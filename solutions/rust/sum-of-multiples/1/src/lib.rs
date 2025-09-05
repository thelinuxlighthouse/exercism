use std::collections::HashSet;

pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    if limit == 1 || factors.is_empty() {
        0
    } else {
        let mut energy_points = HashSet::new();
        for factor in factors.iter() {
            if *factor != 0 {
                let mut f = 1;
                while f * factor < limit {
                    energy_points.insert(f * factor);
                    f += 1;
                }
            } else {
                break;
            }
        }
        energy_points.iter().fold(0, |acc, x| acc + *x)
    }
}
