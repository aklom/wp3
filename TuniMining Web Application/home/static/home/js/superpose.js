
var category = -1;
var subcategory = -1;
var entity = -1;

var items = [
    ["Art",
        ["Music", ["Balti", "Manel Amara", "Hassen Doss", "Zina Gasrinia", "Samara", "Kafon", "Emel Mathlouthi", "Akrem Mag", "A.L.A"]],
        ["Cinema", ["Hend Sabri", "Dhafer Abidine", "Fathi Haddaoui", "Dorra Zarrouk", "Aicha Attia", "Mohamed Ali Nahdi"]]
    ],
    ["Business",
        ["Companies", ["Tunisie Telecom", "Ooredoo", "Orange", "Tunisair", "Nouvelair", "Hamadi Abid", "Vitalait", "Sasio"]],
        ["Banks", ["ATB", "Amen Bank", "Banque de l'habitat", "Attijari Bank", "Banque Zitouna", "UBCI", "Banque de Tunisie", "Banque Centrale"]]
    ],
    ["Politics",
        ["Well-known persons", ["Beji Caid Essebsi", "Youssef Chahed", "Rached Ghannouchi", "Slim Riahi", "Hamma Hammami", "Fadhel Moussa", "Sihem Ben Sedrine", "Noureddine Tabboubi"]],
        ["Political Parties", ["Nidaa Tounes", "Ennahdha", "Al massar", "Courant démocratique", "Afek Tounes", "Parti des  travailleurs"]]
    ],
    ["Sport",
        ["Players", ["Oussama Melllouli", "Habiba Ghribi", "Ons Jabeur", "Malek Jaziri", "Azza Besbes", "Yassine Chikhaoui", "Youssef Msekni", "Wissem Hmem"]],
        ["Clubs", ["EST", "CSS", "CA", "ESS", "CAB"]]
    ],
    ["Entertainment",
        ["Shows", ["Labes", "Hikayet Tounsia", "Oumour Jedia", "Ma lam youkal", "Dimanche Hannibal", "360 Degrés", "Ala Tarik", "Dlilek Mlak"]],
        ["TV Stars", ["Sami Fehri", "Abderrazek Chebbi", "Ala Chebbi", "Naoufel Wartani", "Lotfi Abdelli", "Haythem El Mekki", "Amine Gara", "Maya Ksouri", "Lotfi Amari"]]
    ]


]

function home() {
    document.getElementById("home").style.visibility = "hidden";
    document.getElementById("search").style.visibility = "hidden";
    document.getElementById("categories").style.visibility = "visible";
    for (var i = 1; i <= items.length; i++){
        document.getElementById("cat" + i).innerHTML = items[i - 1][0];
    }
}

function cat(c) {
    category = c;
    var subcategories = [];
    for (var i = 1; i < items[c].length; i++){
        subcategories.push(items[c][i][0]);
    }

    document.getElementById("categories").style.visibility = "hidden";
    document.getElementById("subcategories").style.visibility = "visible";
    for (var i = 1; i <= subcategories.length; i++){
        document.getElementById("sub" + i).innerHTML = subcategories[i - 1];
    }
}

function sub(c) {
    subcategory = c;
    var entities = items[category][subcategory + 1][1];

    document.getElementById("subcategories").style.visibility = "hidden";
    document.getElementById("entities").style.visibility = "visible";
    for (var i = 1; i <= entities.length; i++){
        document.getElementById("ent" + i).innerHTML = entities[i - 1];
    }

    for(var i = entities.length + 1; i <= 9; i++){
        document.getElementById("ent" + i).style.visibility = "hidden";
    }
}

function ent(c) {
    entity = c;
    document.getElementById("entities").style.visibility = "hidden";
    document.getElementById("wait").style.visibility = "visible";
    entityname = items[category][subcategory + 1][1][c];
    document.getElementById("input").value = entityname;
    document.getElementById("form").submit();

}

function back(i){
    if(i == 0){
        document.getElementById("home").style.visibility = "visible";
        document.getElementById("search").style.visibility = "visible";
        document.getElementById("categories").style.visibility = "hidden";
    }

    if(i == 1){
        subcategory = -1;
        document.getElementById("subcategories").style.visibility = "hidden";
        document.getElementById("categories").style.visibility = "visible";
    }

    if(i == 2){
        entity = -1;
        document.getElementById("entities").style.visibility = "hidden";
        document.getElementById("subcategories").style.visibility = "visible";
    }


}
