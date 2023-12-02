use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
//use regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn is_success(game_line:&str) -> bool {
    let no_game = game_line.split(": ").collect::<Vec<&str>>().into_iter().nth(1).unwrap();
    let all_commas = str::replace(no_game, ";",",");
    let all_numbers = all_commas.split(", ").collect::<Vec<&str>>();

    for num in all_numbers {
        let count = num.split(" ")
                       .collect::<Vec<&str>>()
                       .first()
                       .unwrap()
                       .to_string()
                       .parse::<i32>()
                       .unwrap();
        let color = num.split(" ")
                       .collect::<Vec<&str>>()
                       .last()
                       .unwrap()
                       .to_string();
        if color == "red" && count > 12 {
            return false
        }
        if color == "green" && count > 13 {
            return false
        }
        if color == "blue" && count > 14 {
            return false
        }
    }
    return true
}

fn calc_power(game_line:&str) -> i32 {
    let no_game = game_line.split(": ").collect::<Vec<&str>>().into_iter().nth(1).unwrap();
    let all_commas = str::replace(no_game, ";",",");
    let all_numbers = all_commas.split(", ").collect::<Vec<&str>>();

    let mut max_red = 0;
    let mut max_green = 0;
    let mut max_blue = 0;

    for num in all_numbers {
        let count = num.split(" ")
                       .collect::<Vec<&str>>()
                       .first()
                       .unwrap()
                       .to_string()
                       .parse::<i32>()
                       .unwrap();
        let color = num.split(" ")
                       .collect::<Vec<&str>>()
                       .last()
                       .unwrap()
                       .to_string();

        if color == "red" && count > max_red {
            max_red = count;
        }
        if color == "green" && count > max_green {
            max_green = count;
        }
        if color == "blue" && count > max_blue {
            max_blue = count;
        }
    }

    return max_red*max_blue*max_green
}


fn main() {
    let mut total_success = 0;
    let mut total_power = 0;
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day02_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for (i, line) in lines.enumerate() {
            if let Ok(line_value) = line {
                if is_success(&line_value) {
                    total_success += i+1;
                }
                total_power += calc_power(&line_value);
            }
        }
    }
    
    println!("Total success: {}",total_success);
    println!("Total power: {}",total_power);
}
