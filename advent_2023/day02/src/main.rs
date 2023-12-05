use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use fancy_regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn evaluate_game(game_line:&str) -> (i32, i32) {
    let mut c_max:Vec<i32> = vec![];

    for color in vec!["red","green","blue"] {
        let c_re =  Regex::new(&("[0-9]{1,5}(?= ".to_owned()+&color.to_string()+")")).unwrap();
        let c_val = *c_re.find_iter(game_line)
        .filter_map(|cap| cap.unwrap().as_str().parse().ok())
        .collect::<Vec<i32>>().iter().max().unwrap();
        c_max.push(c_val);
    }

    let valid = if c_max[0] <= 12 && c_max[1] <= 13 && c_max[2] <= 14 {1} else {0};
    let power = c_max[0] * c_max[1] * c_max[2];

    return (valid, power)
   
}


fn main() {
    let mut total_success = 0;
    let mut total_power = 0;
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day02_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for (i, line) in lines.enumerate() {
            if let Ok(line_value) = line {
                let (valid, power) = evaluate_game(&line_value);
                if valid > 0 {total_success+=i+1};
                total_power += power;
            }
        }
    }
    
    println!("Total success: {}", total_success);
    println!("Total power: {}", total_power);
}
