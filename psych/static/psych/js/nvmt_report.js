$(document).ready(function(){
    // $('.modal').modal();
    // $('select').formSelect();
    init();
});

function loadTableData(test_data, trialClicks) {
    loadAllTable(test_data, trialClicks);
    loadSimpleTable(test_data, trialClicks);
    loadComplexTable(test_data, trialClicks);
}

function init() {
    let test_data = JSON.parse($('input#test_data').val());
    let trial_clicks = [];
    for (let trial of test_data.trials) {
        let num_clicks = 0;
        for (let card of trial.cards) {
            num_clicks += card.num_clicks;
        }
        trial_clicks.push({name: trial.trial_num, data: num_clicks});
    }
    let total_distance = 0;
    let simple_card_totals = [];
    for (let trial = 1; trial < test_data.trials.length-1; trial+=1) {
        let simple_distance_total = 0;
        for (let card of test_data.trials[trial].cards) {
            for (let distance of card.target_distances) {
                if (card.card_num == 1 || card.card_num == 3 || card.card_num == 5) {
                    simple_distance_total += distance;
                } 
                total_distance += distance;
            }
        }
        simple_card_totals.push(simple_distance_total);
    }
    loadTableData(test_data, trial_clicks);
    loadBiasedTables(test_data, total_distance, simple_card_totals);
    
    let trial_distances = [];
    for (let trial of test_data.trials) {
        let cards = [];
        for (let card of trial.cards) {
            let distance_total = 0;
            for (let distance of card.target_distances) {
                distance_total += distance;
            }
            cards.push({name: card.card_num, data: distance_total});
        }
        trial_distances.push(cards);
    }
    var clicks_data = {
        labels: ['1', '2', '3', '4', '5', '6'],
        series: [trial_clicks]
    };

    var distance_data = {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
        series: [
            {
                name: 'Trial #1',
                data: trial_distances[0]
            },
            {
                name: 'Trial #2',
                data: trial_distances[1]
            },
            {
                name: 'Trial #3',
                data: trial_distances[2]
            },
            {
                name: 'Trial #4',
                data: trial_distances[3]
            },
            {
                name: 'Trial #5',
                data: trial_distances[4]
            },
            {
                name: 'Trial #6',
                data: trial_distances[5]
            }
        ]
    };
    
    let click_options = {
        height: 500,
        width: 1000,
        seriesBarDistance: 50,
        lineSmooth: false,
        axisX: {
            labelInterpolationFnc: function(value) {
            return 'Trial #' + value;
            }
        },
        // Y-Axis specific configuration
        axisY: {
            // Lets offset the chart a bit from the labels
            offset: 120,
            type: Chartist.AutoScaleAxis,
            onlyInteger: true,
            // The label interpolation function enables you to modify the values
            // used for the labels on each axis. Here we are converting the
            // values into million pound.
            labelInterpolationFnc: function(value) {
                return value + ' clicks';
            }
        }
    };

    let distance_options = {
        height: 500,
        width: 1000,
        seriesBarDistance: 50,
        showArea: true,
        lineSmooth: false,
        axisX: {
            labelInterpolationFnc: function(value) {
            return 'Card #' + value;
            }
        },
        // Y-Axis specific configuration
        axisY: {
            // Lets offset the chart a bit from the labels
            offset: 120,
            type: Chartist.AutoScaleAxis,
            onlyInteger: true,
            // The label interpolation function enables you to modify the values
            // used for the labels on each axis. Here we are converting the
            // values into million pound.
            labelInterpolationFnc: function(value) {
                return value + 'px';
            }
        }
    };

    new Chartist.Line('#num_clicks_chart', clicks_data, click_options);
    new Chartist.Line('#distances_chart', distance_data, distance_options);
}

function loadSimpleTable(test_data, trialClicks){
    let allTable = $('#allSimpleScores');

    for (let trial in trialClicks) {
        let trialData = test_data.trials[trial];
        let row = document.createElement('tr');

        let trialCol = document.createElement('td');
        let rawCol = document.createElement('td');
        let meanCol = document.createElement('td');
        let sdCol = document.createElement('td');
        let tCol = document.createElement('td');

        let raw = trialClicks[trial].data;
        let mean = trialData.simpleValues.mean;
        let sd = trialData.simpleValues.sd;
        let t = (((raw-mean)/sd)*10) + 50;
        
        let trialText = null;
        if (trial == 5) {
            trialText = document.createTextNode("Retest");
        }
        else {
            trialText = document.createTextNode("Trial " + (Number.parseInt(trial)+1));
        }
        let rawText = document.createTextNode(raw);
        let meanText = document.createTextNode(mean);
        let sdText = document.createTextNode(sd);
        let tText = document.createTextNode(t.toPrecision(4));

        trialCol.appendChild(trialText);
        rawCol.appendChild(rawText);
        meanCol.appendChild(meanText);
        sdCol.appendChild(sdText);
        tCol.appendChild(tText);
        
        row.appendChild(trialCol);
        row.appendChild(rawCol);
        row.appendChild(meanCol);
        row.appendChild(sdCol);
        row.appendChild(tCol);

        allTable.append(row);
    }
}
function loadComplexTable(test_data, trialClicks) {
    let allTable = $('#allComplexScores');

    for (let trial in trialClicks) {
        let trialData = test_data.trials[trial];
        let row = document.createElement('tr');

        let trialCol = document.createElement('td');
        let rawCol = document.createElement('td');
        let meanCol = document.createElement('td');
        let sdCol = document.createElement('td');
        let tCol = document.createElement('td');

        let raw = trialClicks[trial].data;
        let mean = trialData.complexValues.mean;
        let sd = trialData.complexValues.sd;
        let t = (((raw-mean)/sd)*10) + 50;
        
        let trialText = null;
        if (trial == 5) {
            trialText = document.createTextNode("Retest");
        }
        else {
            trialText = document.createTextNode("Trial " + (Number.parseInt(trial)+1));
        }

        let rawText = document.createTextNode(raw);
        let meanText = document.createTextNode(mean);
        let sdText = document.createTextNode(sd);
        let tText = document.createTextNode(t.toPrecision(4));

        trialCol.appendChild(trialText);
        rawCol.appendChild(rawText);
        meanCol.appendChild(meanText);
        sdCol.appendChild(sdText);
        tCol.appendChild(tText);
        
        row.appendChild(trialCol);
        row.appendChild(rawCol);
        row.appendChild(meanCol);
        row.appendChild(sdCol);
        row.appendChild(tCol);

        allTable.append(row);
    }
}

function loadAllTable(test_data, trialClicks) {
    let allTable = $('#allCardsScores');

    for (let trial in trialClicks) {
        let trialData = test_data.trials[trial];
        let row = document.createElement('tr');

        let trialCol = document.createElement('td');
        let rawCol = document.createElement('td');
        let meanCol = document.createElement('td');
        let sdCol = document.createElement('td');
        let tCol = document.createElement('td');
        
        let raw = trialClicks[trial].data;
        let mean = trialData.originalValues.mean;
        let sd = trialData.originalValues.sd;
        let t = (((raw-mean)/sd)*10) + 50;
        
        let trialText = null;
        if (trial == 5) {
            trialText = document.createTextNode("Retest");
        }
        else {
            trialText = document.createTextNode("Trial " + (Number.parseInt(trial)+1));
        }

        let rawText = document.createTextNode(raw);
        let meanText = document.createTextNode(mean);
        let sdText = document.createTextNode(sd);
        let tText = document.createTextNode(t.toPrecision(4));

        trialCol.appendChild(trialText);
        rawCol.appendChild(rawText);
        meanCol.appendChild(meanText);
        sdCol.appendChild(sdText);
        tCol.appendChild(tText);
        
        row.appendChild(trialCol);
        row.appendChild(rawCol);
        row.appendChild(meanCol);
        row.appendChild(sdCol);
        row.appendChild(tCol);

        allTable.append(row);
    }
}

function loadBiasedTables(test_data, total_distance, simple_card_totals) {
    let norms = test_data.biased_norms.total;
    let totalBiasedTable = $("#totalBiasedTable");

    let row = document.createElement('tr');
    
    let trialsCol = document.createElement('td');
    let minCol = document.createElement('td');
    let maxCol = document.createElement('td');
    let meanCol = document.createElement('td');
    let sdCol = document.createElement('td');
    let scoreCol = document.createElement('td');
    let biasedCol = document.createElement('td');

    let trialsText = document.createTextNode("Trials 2-5");
    let minText = document.createTextNode(norms.min);
    let maxText = document.createTextNode(norms.max);
    let meanText = document.createTextNode(norms.mean);
    let sdText = document.createTextNode(norms.sd);
    let distanceText = document.createTextNode(total_distance.toPrecision(6));
    let biasedText = null;
    
    if (total_distance >= norms.mean + (2*norms.sd)) {
        biasedText = document.createTextNode("Feigning Probability: 99%");
    } 
    else if (total_distance >= norms.mean + (1.5*norms.sd)) {
        biasedText = document.createTextNode("Feigning Probability: 95%");
    }
    else {
        biasedText = document.createTextNode("No Signs of Feigning");
    }

    trialsCol.appendChild(trialsText);
    minCol.appendChild(minText);
    maxCol.appendChild(maxText);
    meanCol.appendChild(meanText);
    sdCol.appendChild(sdText);
    scoreCol.append(distanceText);
    biasedCol.appendChild(biasedText);

    row.appendChild(trialsCol);
    row.appendChild(minCol);
    row.appendChild(maxCol);
    row.appendChild(meanCol);
    row.appendChild(sdCol);
    row.appendChild(scoreCol);
    row.appendChild(biasedCol);
    
    totalBiasedTable.append(row);

    // doing simple biased table now
    let simpleNorms = test_data.biased_norms.simple;
    let simpleBiasedTable = $("#simpleBiasedTable");

    let trialCounter = 2;
    for (let trial of simple_card_totals) {
        let row = document.createElement('tr');
    
        let trialsCol = document.createElement('td');
        let minCol = document.createElement('td');
        let maxCol = document.createElement('td');
        let meanCol = document.createElement('td');
        let sdCol = document.createElement('td');
        let scoreCol = document.createElement('td');
        let biasedCol = document.createElement('td');

        let trialsText = document.createTextNode("Trial #" + trialCounter);
        let minText = document.createTextNode(simpleNorms.min);
        let maxText = document.createTextNode(simpleNorms.max);
        let meanText = document.createTextNode(simpleNorms.mean);
        let sdText = document.createTextNode(simpleNorms.sd);
        let distanceText = document.createTextNode(trial);
        let biasedText = null;

        if (trial > norms.mean + (2*norms.sd)) {
            biasedText = document.createTextNode("Feigning Probability: 99%");
        } 
        else if (total_distance >= norms.mean + (1.5*norms.sd)) {
            biasedText = document.createTextNode("Feigning Probability: 95%");
        }
        else {
            biasedText = document.createTextNode("No Signs of Feigning");
        }

        trialsCol.appendChild(trialsText);
        minCol.appendChild(minText);
        maxCol.appendChild(maxText);
        meanCol.appendChild(meanText);
        sdCol.appendChild(sdText);
        scoreCol.append(distanceText);
        biasedCol.appendChild(biasedText);

        row.appendChild(trialsCol);
        row.appendChild(minCol);
        row.appendChild(maxCol);
        row.appendChild(meanCol);
        row.appendChild(sdCol);
        row.appendChild(scoreCol);
        row.appendChild(biasedCol);

        simpleBiasedTable.append(row);
        trialCounter += 1;
    }
}