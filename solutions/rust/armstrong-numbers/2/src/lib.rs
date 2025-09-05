pub fn is_armstrong_number(num: u32) -> bool {
    let num = u64::from(num);
    let num_count = num.to_string().len() as u32;
    let mut sum: u64 = 0;
    for i in num.to_string().chars(){
        sum += u64::pow(i.to_digit(10).unwrap() as u64, num_count);
    }
    sum == num
}
