pub fn is_armstrong_number(num: u32) -> bool {
    let num_count = num.to_string().len() as u32;
    let mut sum: u32 = 0;
    for i in num.to_string().chars(){
        sum += u32::pow(i.to_digit(10).unwrap(), num_count);
    }
    sum == num
}
