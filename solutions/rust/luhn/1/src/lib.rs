/// Check a Luhn checksum.
pub fn is_valid(code: &str) -> bool {
    let binding = code.to_string();
    let code_vec = binding.trim().split(' ').filter(|s| !s.is_empty()).collect::<Vec<_>>();
    let code = String::from_iter(code_vec);

    let mut luhn_vec: Vec<i64>;

    if code.len() <= 1 || code.parse::<i64>().is_err() || code.is_empty() {
        false
    } else {
        luhn_vec = code
            .chars()
            .map(|s| s.to_string().parse::<i64>().unwrap())
            .collect();
        let luhn_vec_len = luhn_vec.len();

        let mut i: usize = 2;
        while i < luhn_vec_len + 1 {
            if luhn_vec[luhn_vec_len - i] * 2 > 9 {
                luhn_vec[luhn_vec_len - i] = (luhn_vec[luhn_vec_len - i] * 2) - 9;
            } else {
                luhn_vec[luhn_vec_len - i] *= 2;
            }
            i += 2;
        }
        luhn_vec.iter().sum::<i64>() % 10 == 0
    }
}
