pub fn int_to_roman(num: i32) -> String {
    let mut number = num;
    let mut ans = String::new();

    // Define the mapping of Roman numerals to their integer values
    let values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ];

    // Iterate over the mapping and build the Roman numeral
    for &(val, roman) in values.iter() {
        while number >= val {
            number -= val;
            ans.push_str(roman);
        }
    }

    ans
}

fn main(){
    println!("{}", int_to_roman(3005))
}