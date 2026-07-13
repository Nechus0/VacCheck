let drugsDatabase = [];
const selectedDrugs = [];

// DOM Elements
const inputElement = document.getElementById('drugInput');
const autocompleteList = document.getElementById('autocomplete-list');
const selectedDrugsList = document.getElementById('selectedDrugsList');

// Fetch the drug database
fetch('app_drugs_db.json')
    .then(response => response.json())
    .then(data => {
        drugsDatabase = data;
        console.log(`Loaded ${drugsDatabase.length} drugs.`);
    })
    .catch(error => console.error('Error loading drug database:', error));

// Event listeners for autocomplete
inputElement.addEventListener('input', function() {
    let val = this.value;
    
    closeAllLists();
    currentFocus = -1;
    
    if (!val) { return false; }

    let count = 0;
    
    // Create new list container
    const listContainer = document.createElement('div');
    listContainer.setAttribute('class', 'autocomplete-items');
    this.parentNode.appendChild(listContainer);

    let matches = [];

    for (let i = 0; i < drugsDatabase.length; i++) {
        const drug = drugsDatabase[i];
        
        // Search in substance and brand names
        let matchText = '';
        let isStartsWith = false;
        let isBrandMatch = false;

        const valLower = val.toLowerCase();
        const substanceLower = drug.substance.toLowerCase();

        if (substanceLower.includes(valLower)) {
            matchText = drug.substance;
            if (substanceLower.startsWith(valLower)) {
                isStartsWith = true;
            }
        } else {
            const matchedBrand = drug.brand_names.find(b => b.toLowerCase().includes(valLower));
            if (matchedBrand) {
                matchText = `${matchedBrand} (${drug.substance})`;
                isBrandMatch = true;
                if (matchedBrand.toLowerCase().startsWith(valLower)) {
                    isStartsWith = true;
                }
            }
        }

        if (matchText) {
            matches.push({
                drug: drug,
                matchText: matchText,
                isStartsWith: isStartsWith,
                isBrandMatch: isBrandMatch
            });
        }
    }

    // Sort matches: 
    // 1. Starts with input
    // 2. Contains input
    // Alphabetically within groups
    matches.sort((a, b) => {
        if (a.isStartsWith && !b.isStartsWith) return -1;
        if (!a.isStartsWith && b.isStartsWith) return 1;
        return a.matchText.localeCompare(b.matchText);
    });

    // Take top 15 results
    matches = matches.slice(0, 15);

    for (let i = 0; i < matches.length; i++) {
        const itemData = matches[i];
        const drug = itemData.drug;
        const item = document.createElement('div');
        item.setAttribute('class', 'autocomplete-item');
        
        // Highlight matching part
        const regex = new RegExp(`(${val})`, 'gi');
        item.innerHTML = itemData.matchText.replace(regex, "<strong>$1</strong>");

        item.addEventListener('click', function() {
            addDrug(drug);
            inputElement.value = '';
            closeAllLists();
        });

        listContainer.appendChild(item);
    }
});

let currentFocus = -1;

inputElement.addEventListener('keydown', function(e) {
    const listContainer = document.getElementById('autocomplete-list');
    if (!listContainer) return;
    
    let items = listContainer.getElementsByClassName('autocomplete-item');
    if (e.key === 'ArrowDown') {
        currentFocus++;
        addActive(items);
    } else if (e.key === 'ArrowUp') {
        currentFocus--;
        addActive(items);
    } else if (e.key === 'Enter') {
        e.preventDefault();
        if (currentFocus > -1) {
            if (items) items[currentFocus].click();
        } else if (items.length > 0) {
            items[0].click(); // Select first item if nothing is focused
        }
    }
});

function addActive(items) {
    if (!items) return false;
    removeActive(items);
    if (currentFocus >= items.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (items.length - 1);
    items[currentFocus].classList.add('active-item');
}

function removeActive(items) {
    for (let i = 0; i < items.length; i++) {
        items[i].classList.remove('active-item');
    }
}

function closeAllLists(elmnt) {
    const x = document.getElementsByClassName('autocomplete-items');
    for (let i = 0; i < x.length; i++) {
        if (elmnt != x[i] && elmnt != inputElement) {
            x[i].parentNode.removeChild(x[i]);
        }
    }
}

document.addEventListener('click', function (e) {
    closeAllLists(e.target);
});

function addDrug(drug) {
    // Prevent duplicates
    if (selectedDrugs.find(d => d.substance === drug.substance)) {
        return;
    }
    
    selectedDrugs.push(drug);
    renderSelectedDrugs();
}

function removeDrug(substance) {
    const index = selectedDrugs.findIndex(d => d.substance === substance);
    if (index > -1) {
        selectedDrugs.splice(index, 1);
        renderSelectedDrugs();
    }
}

function renderSelectedDrugs() {
    if (selectedDrugs.length === 0) {
        selectedDrugsList.innerHTML = '<p class="empty-state">Noch keine Medikamente ausgewählt.</p>';
        return;
    }

    selectedDrugsList.innerHTML = '';
    
    selectedDrugs.forEach(drug => {
        const card = document.createElement('div');
        card.className = `drug-card ${drug.is_immunosuppressant ? 'immunosuppressant' : ''}`;
        
        let brandsHTML = '';
        if (drug.brand_names && drug.brand_names.length > 0) {
            brandsHTML = `<div class="drug-brands">Handelsnamen: ${drug.brand_names.join(', ')}</div>`;
        }

        let detailsHTML = '';
        if (drug.is_immunosuppressant) {
            let classHTML = '';
            if (drug.drug_class) {
                let abstractHTML = '';
                if (drug.class_abstract) {
                    abstractHTML = `<div style="font-size: 12px; font-style: italic; color: #666; margin-top: 4px;">${drug.class_abstract}</div>`;
                }
                classHTML = `
                    <div class="detail-item" style="grid-column: span 2; margin-bottom: 8px;">
                        <div class="detail-label">Substanzklasse</div>
                        <div style="font-weight: 500;">${drug.drug_class}</div>
                        ${abstractHTML}
                    </div>
                `;
            }
            detailsHTML = `
                <div class="drug-details">
                    ${classHTML}
                    <div class="detail-item">
                        <div class="detail-label">Lebendimpfung</div>
                        <div>${drug.live_vaccine_allowed}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Therapiepause (Lebendimpf.)</div>
                        <div>${drug.therapy_pause_needed}</div>
                    </div>
                    <div class="detail-item" style="grid-column: span 2;">
                        <div class="detail-label">Immunantwort auf Totimpfstoffe</div>
                        <div>${drug.immune_response_dead_vaccine}</div>
                    </div>
                </div>
            `;
        } else {
            detailsHTML = `
                <div class="drug-details">
                    <div class="detail-item" style="grid-column: span 2;">
                        <div class="detail-label">Status</div>
                        <div style="color: var(--safe); font-weight:600;">Keine bekannten Kontraindikationen für Lebendimpfungen aus der DTG 2026 Leitlinie.</div>
                    </div>
                </div>
            `;
        }

        const warningBadge = drug.is_immunosuppressant ? '<span class="warning-badge">Immunsuppressivum</span>' : '';

        card.innerHTML = `
            <div class="drug-header">
                <div>
                    <div class="drug-title">${drug.substance} ${warningBadge}</div>
                    ${brandsHTML}
                </div>
                <button class="remove-btn" onclick="removeDrug('${drug.substance}')">&times;</button>
            </div>
            ${detailsHTML}
        `;
        
        selectedDrugsList.appendChild(card);
    });
}
