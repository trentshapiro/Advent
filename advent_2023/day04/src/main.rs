use std::fs;

fn read_file(path: &str) -> String {
    return fs::read_to_string(path).expect("Could not read file.");
}

fn line_operation(line: &str) {
    return;
}

fn main() {
    let file_path = "/mnt/c/workspace/Advent/advent_2023/day04/day04_input_sample.txt";
    let contents = read_file(file_path);

    for line in contents.split("\n") {
        println!("\n{line}");
    }
}
