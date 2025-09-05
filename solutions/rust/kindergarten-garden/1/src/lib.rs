use std::collections::HashMap;

pub fn plants(diagram: &str, student: &str) -> Vec<&'static str> {
    let students = HashMap::from([
        ("Alice", [0, 1]),
        ("Bob", [2, 3]),
        ("Charlie", [4, 5]),
        ("David", [6, 7]),
        ("Eve", [8, 9]),
        ("Fred", [10, 11]),
        ("Ginny", [12, 13]),
        ("Harriet", [14, 15]),
        ("Ileana", [16, 17]),
        ("Joseph", [18, 19]),
        ("Kincaid", [20, 21]),
        ("Larry", [22, 23]),
    ]);

    let plants_apprv: HashMap<char, &str> = HashMap::from([
        ('G', "grass"),
        ('C', "clover"),
        ('R', "radishes"),
        ('V', "violets"),
    ]);

    let rows = String::from(diagram);

    let digram_split: Vec<_> = rows.split('\n').collect();

    let mut plants_to_yield: Vec<&'static str> = Vec::new();
    let std_pos = students[student];

    for items in digram_split {
        plants_to_yield.push(plants_apprv[&items.chars().nth(std_pos[0]).unwrap()]);
        plants_to_yield.push(plants_apprv[&items.chars().nth(std_pos[1]).unwrap()]);
    }

    plants_to_yield
}
