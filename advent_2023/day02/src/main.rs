use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn get_game_number(game_line:&str) -> &str {
    let first_split = game_line.split(":").collect().into_iter().nth(0);
    let second_split = first_split.split(" ").unwrap().collect::<Vec<&str>>().last();
    println!("{}",second_split);

    return second_split
}

fn main() {
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day02_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(line_value) = line {
                println!("{}", &line_value);
                println!("{}", get_game_number(&line_value));
            }
        }
    }
}
