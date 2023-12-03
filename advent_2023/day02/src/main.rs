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
    let re_r = Regex::new("[0-9]{1,5}(?= red)").unwrap();
    let re_g = Regex::new("[0-9]{1,5}(?= green)").unwrap();
    let re_b = Regex::new("[0-9]{1,5}(?= blue)").unwrap();

    let max_r: i32 = *re_r.find_iter(game_line)
        .filter_map(|cap| cap.unwrap().as_str().parse::<i32>().ok())
        .collect::<Vec<i32>>().iter().max().unwrap();

    let max_g: i32 = *re_g.find_iter(game_line)
        .filter_map(|cap| cap.unwrap().as_str().parse::<i32>().ok())
        .collect::<Vec<i32>>().iter().max().unwrap();

    let max_b: i32 = *re_b.find_iter(game_line)
        .filter_map(|cap| cap.unwrap().as_str().parse::<i32>().ok())
        .collect::<Vec<i32>>().iter().max().unwrap();

    
    let valid = if max_r <= 12 && max_g <= 13 && max_b <= 14 {1} else {0};
    let power = max_r * max_g * max_b;

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
