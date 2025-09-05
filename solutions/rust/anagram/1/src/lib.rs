use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let mut hash_set = HashSet::<&'a str>::new();
    
    let mut word_sorted: Vec<char> = word.to_lowercase().chars().collect();
    
    word_sorted.sort_by(|a, b| b.cmp(a));
    
    for item in possible_anagrams {
        if word.to_string().to_lowercase() == item.to_string().to_lowercase() {
            continue;
        }
        let mut pos_ang: Vec<char> = item.to_lowercase().chars().collect();
        pos_ang.sort_by(|a, b| b.cmp(a));
        if pos_ang == word_sorted {
            hash_set.insert(item);
        }
    }
    hash_set
}
