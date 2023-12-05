use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use fancy_regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn row_value(mixed_string: &str) -> i32{
    let row_re = Regex::new(r"[0-9]{1,1}").unwrap();
    let row_digits = row_re.find_iter(mixed_string)
        .filter_map(|cap| cap.unwrap().as_str().parse().ok())
        .collect::<Vec<i32>>();

    let (a,b) = (row_digits.first().unwrap(), row_digits.last().unwrap());

    return a*10+b

}

fn sanitize_str(mixed_string: &str) -> String {
    let mut string_out = mixed_string.to_string();
    let num_words = vec!["one","two","three","four","five","six","seven","eight","nine"];
    for (idx, num_word) in num_words.iter().enumerate(){
        let fixed_str = num_word.to_string().chars().nth(0).unwrap().to_string() +
                        &(idx+1).to_string() + 
                        &num_word.to_string().chars().last().unwrap().to_string();
        string_out = string_out.replace(num_word, &fixed_str)
    }
    return string_out
}

fn main() {
    let mut running_total = 0;
    let mut fixed_total = 0;
    // File must exist in the current path
    if let Ok(lines) = read_lines("./day01_input.txt") {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(line_value) = line {
                //println!("{}", &line_value);
                running_total += row_value(&line_value);
                fixed_total += row_value(&sanitize_str(&line_value));
            }
        }
    }
    println!("{}", running_total);
    println!("{}", fixed_total);

}

