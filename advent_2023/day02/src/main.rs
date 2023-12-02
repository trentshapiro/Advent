use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
//use regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn evaluate_game(game_line:&str) -> Vec<i32> {
    let no_game = game_line.split(": ").collect::<Vec<&str>>().into_iter().nth(1).unwrap();
    let all_commas = str::replace(no_game, ";",",");
    let all_numbers = all_commas.split(", ").collect::<Vec<&str>>();

    let mut max_red = 0;
    let mut max_green = 0;
    let mut max_blue = 0;
    let mut valid = 1;

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

        if color == "red" {
            if count > 12 {
                valid = 0;
            }
            if count > max_red {
                max_red = count;
            }
        } else if color == "green" {
            if count > 13 {
                valid = 0;
            }
            if count > max_green {
                max_green = count;
            }
        } else if color == "blue" {
            if count > 14 {
                valid = 0;
            }
            if count > max_blue {
                max_blue = count;
            }
        }
    }

    return vec![valid, max_red*max_blue*max_green]
}


fn main() {
    let mut total_success = 0;
    let mut total_power = 0;
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day02_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for (i, line) in lines.enumerate() {
            if let Ok(line_value) = line {
                let rets = evaluate_game(&line_value);
                if rets.first().unwrap() > &0 {
                    total_success += i+1;
                }
                total_power += rets.last().unwrap();
            }
        }
    }
    
    println!("Total success: {}",total_success);
    println!("Total power: {}",total_power);
}
