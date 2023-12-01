use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

// fn first_digit(mixed_string: &str) -> i32 {
//     for c in mixed_string.chars() {
//         if c.is_numeric() {
//             return c as i32 - 0x30
//         }
//     }
//     return 0
// }

fn first_digit_with_words(mixed_str: &str) -> i32 {
    let start_list = mixed_str.chars();
    let mut build_str = String::from("");

    for c in start_list {
        // see if we have a number already
        if c.is_numeric() {
            return c as i32 - 0x30
        };
        // add current character to list, check for word
        build_str.push(c);
        //println!("{}", build_str);
        let res = match build_str{
            ref build_str if build_str.contains("one")   => 1,
            ref build_str if build_str.contains("two")   => 2,
            ref build_str if build_str.contains("three") => 3,
            ref build_str if build_str.contains("four")  => 4,
            ref build_str if build_str.contains("five")  => 5,
            ref build_str if build_str.contains("six")   => 6,
            ref build_str if build_str.contains("seven") => 7,
            ref build_str if build_str.contains("eight") => 8,
            ref build_str if build_str.contains("nine")  => 9,
            _ => 0
        };
        if res > 0{
            return res
        };
    }

    return 0

}

// fn last_digit(mixed_string: &str) -> i32 {
//     for c in mixed_string.chars().rev() {
//         if c.is_numeric() {
//             return c as i32 - 0x30
//         }
//     }
//     return 0
// }

fn last_digit_with_words(mixed_str: &str) -> i32 {
    let start_list = mixed_str.chars().rev();
    let mut build_str = String::from("");

    for c in start_list {
        // see if we have a number already
        if c.is_numeric() {
            return c as i32 - 0x30
        };
        // add current character to list, check for word
        build_str.push(c);
        //println!("{}", build_str);
        let res = match build_str{
            ref build_str if build_str.contains("eno")   => 1,
            ref build_str if build_str.contains("owt")   => 2,
            ref build_str if build_str.contains("eerht") => 3,
            ref build_str if build_str.contains("ruof")  => 4,
            ref build_str if build_str.contains("evif")  => 5,
            ref build_str if build_str.contains("xis")   => 6,
            ref build_str if build_str.contains("neves") => 7,
            ref build_str if build_str.contains("thgie") => 8,
            ref build_str if build_str.contains("enin")  => 9,
            _ => 0
        };
        if res > 0{
            return res
        };
    }

    return 0

}

fn main() {
    let mut first;
    let mut second;
    let mut running_total = 0;
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day01_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", &ip);
                first = first_digit_with_words(&ip);
                second = last_digit_with_words(&ip);
                running_total = running_total + first*10 + second;
                println!("{} {} {}", first, second, running_total);
            }
        }
    }
}

