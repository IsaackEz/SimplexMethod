//Table for maximization
// var Table = [
//     [0, 4, 1, 4],
//     [0, 6, 10, 23],
//     [0, 1, 6, 6],
//     [1, 15, 24, 0],
// ];

// //Table for minimization
var Table = [
    [4, 1, 4], //Slack variables
    [6, 10, 23], //Slack variables
    [1, 6, 6], //Slack variables
    [1, 0, 0], //Constraints
    [0, 1, 0], //Constraints
    [15, 24, 0], //Z
];

var TableT;
//Input manually
var decision = "min";
var variables = 2;

//Input in browser
// var decision = window.prompt("Max or Min: ");
// var variables = window.prompt("No. variables: ");

if (decision == "Max" || decision == "max") {
    max();
    maximization(variables);
} else if (decision == "Min" || decision == "min") {
    TableT = Table[0].map((_, colIndex) => Table.map((row) => row[colIndex]));
    var negTable = TableT.slice(-1)[0];
    for (let i = 0; i < negTable.length; i++) {
        negTable[i] *= -1;
    }
    min();
    minimization(variables);
}

function maximization(variable) {
    var rowX;
    var x;
    var lastRow = Table.slice(-1)[0];
    for (let j = 0; j < variable; j++) {
        var column = [];
        for (let i = 0; i < Table.length; i++) {
            var valueColumn = Table[i][j + 1];
            column.push(valueColumn);
        }
        var sum = column.reduce(function(a, b) {
            return a + b;
        }, 0);
        if (sum == 1) {
            rowX = column.indexOf(1);
            x = Table[rowX][lastRow.length - 1];
        } else {
            x = 0;
        }
        console.log("X" + (j + 1) + ": ", x);
    }
    console.log("Z" + ": ", Table[Table.length - 1][lastRow.length - 1]);
}

function minimization(variable) {
    var x;
    var lastRow = TableT.slice(-1)[0];
    for (let i = 0; i < variable; i++) {
        x = TableT[TableT.length - 1][lastRow.length - 2 - i];
        console.log("X" + (i + 1) + ": ", x);
    }
    console.log("Z" + ": ", TableT[TableT.length - 1][lastRow.length - 1]);
}

function fillNewTable(rows, columns) {
    var newTable = [];
    for (let i = 0; i < rows; i++) {
        newTable[i] = [];
        for (let j = 0; j < columns; j++) {
            newTable[i][j] = [];
        }
    }
    return newTable;
}

function max() {
    var flag = 1;
    while (flag != 0) {
        var radQuot = [];
        var valuePositiveRow = [];
        var positionPositiveRows = [];
        var positionPositiveRow;
        var quotPivot;
        var fPivot;
        var ePivot;
        var lastRow = Table.slice(-1)[0];
        var min_FunZ = Math.min.apply(Math, lastRow);
        var cPivot = lastRow.indexOf(min_FunZ);
        if (min_FunZ < 0) {
            var newTable = fillNewTable(Table.length, Table[0].length);
            var xRows = Table.slice(0, -1);
            for (let i = 0; i < xRows.length; i++) {
                if (xRows[i][cPivot] > 0) {
                    valuePositiveRow.push(xRows[i][cPivot]);
                } else {
                    valuePositiveRow.push(0);
                }
            }
            for (let i = 0; i < valuePositiveRow.length; i++) {
                if (valuePositiveRow[i] > 0) {
                    positionPositiveRows.push(
                        valuePositiveRow.indexOf(valuePositiveRow[i])
                    );
                    radQuot.push(Table[i][lastRow.length - 1] / Table[i][cPivot]);
                    quotPivot = Math.min.apply(Math, radQuot);
                    positionPositiveRow = radQuot.indexOf(quotPivot);
                    fPivot = positionPositiveRows[positionPositiveRow];
                }
            }
            ePivot = Table[fPivot][cPivot];
            for (let i = 0; i < lastRow.length; i++) {
                newTable[fPivot][i] = Table[fPivot][i] / ePivot;
            }

            for (let i = 0; i < Table.length; i++) {
                if (i != fPivot) {
                    for (let j = 0; j < Table[i].length; j++) {
                        newTable[i][j] =
                            Table[i][j] - Table[i][cPivot] * newTable[fPivot][j];
                    }
                }
            }
            console.log(Table);
            console.log(newTable);
        } else {
            flag = 0;
        }
        Table = newTable;
    }
}

function min() {
    var flag = 1;
    while (flag != 0) {
        var radQuot = [];
        var valuePositiveRow = [];
        var positionPositiveRows = [];
        var positionPositiveRow;
        var quotPivot;
        var fPivot;
        var ePivot;
        var lastRow = TableT.slice(-1)[0];
        var min_FunZ = Math.min.apply(Math, lastRow);
        var cPivot = lastRow.indexOf(min_FunZ);
        if (min_FunZ < 0) {
            var newTable = fillNewTable(TableT.length, TableT[0].length);
            var xRows = TableT.slice(0, -1);
            for (let i = 0; i < xRows.length; i++) {
                if (xRows[i][cPivot] > 0) {
                    valuePositiveRow.push(xRows[i][cPivot]);
                } else {
                    valuePositiveRow.push(0);
                }
            }
            for (let i = 0; i < valuePositiveRow.length; i++) {
                if (valuePositiveRow[i] > 0) {
                    positionPositiveRows.push(
                        valuePositiveRow.indexOf(valuePositiveRow[i])
                    );
                    radQuot.push(TableT[i][lastRow.length - 1] / TableT[i][cPivot]);
                    quotPivot = Math.min.apply(Math, radQuot);
                    positionPositiveRow = radQuot.indexOf(quotPivot);
                    fPivot = positionPositiveRows[positionPositiveRow];
                }
            }

            ePivot = TableT[fPivot][cPivot];
            for (let i = 0; i < lastRow.length; i++) {
                newTable[fPivot][i] = TableT[fPivot][i] / ePivot;
            }

            for (let i = 0; i < TableT.length; i++) {
                if (i != fPivot) {
                    for (let j = 0; j < TableT[i].length; j++) {
                        newTable[i][j] =
                            TableT[i][j] - TableT[i][cPivot] * newTable[fPivot][j];
                    }
                }
            }
        } else {
            flag = 0;
        }
        TableT = newTable;
    }
}