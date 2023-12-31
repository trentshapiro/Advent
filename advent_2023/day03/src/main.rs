use std::fs;

struct Point{
    x:i32, 
    y:i32
}

struct Symbol{
    symbol:String, 
    point: Point
}

fn main() {
    let file_path = "day03_input.txt";
    let contents = fs::read_to_string(file_path).expect("Unable to read file");
    let mut numbers = Vec::<Symbol>::new();
    let mut symbols = Vec::<Symbol>::new();
    for (line_num, line) in contents.lines().enumerate(){
        let mut num = String::from("");
        for (pos, ch) in line.chars().enumerate() {
            if ch.is_numeric(){
                num.push(ch);
                if pos == line.len()-1 {
                    numbers.push(
                        Symbol {
                            symbol: num.clone(),
                            point: Point{
                                x: line_num as i32, 
                                y: (pos - num.len()) as i32
                            }
                        }
                    );
                }
            } else {
                if num != "" {
                    numbers.push(
                        Symbol {
                            symbol: num.clone(),
                            point: Point{
                                x: line_num as i32, 
                                y: (pos - num.len()) as i32
                            }
                        }
                    );
                    num = String::from("");
                }
                if ch != '.' {
                    symbols.push(
                        Symbol{
                            symbol:String::from(ch), 
                            point: Point {
                                x:line_num as i32, 
                                y:pos as i32
                            }
                        }
                    );
                }
            }

        }
    }
    let mut part_sum = 0;
    for number in &numbers {
        let mut found = false;
        for symbol in &symbols {
            if (number.point.x - symbol.point.x).abs() > 1 {
                continue
            }
            if (number.point.y - symbol.point.y).abs() < 2 || 
                ((number.point.y + (number.symbol.len() as i32)-1) - symbol.point.y).abs() < 2 {
                found = true;
                break
            }
        }
        if found{
            part_sum+=number.symbol.parse::<i32>().unwrap();
        }
    }
    println!("{}", part_sum);

    let mut ratio = 0;
    for symbol in &symbols {
        let mut touching_nums = Vec::<i32>::new();
        for number in &numbers {
            if (number.point.x - symbol.point.x).abs() > 1 {
                continue
            }
            if (number.point.y - symbol.point.y).abs() < 2 || 
                ((number.point.y + (number.symbol.len() as i32)-1) - symbol.point.y).abs() < 2 {
                touching_nums.push(number.symbol.parse::<i32>().unwrap());
            }
        }
        if touching_nums.len() == 2 {
            ratio += touching_nums.first().unwrap() * touching_nums.last().unwrap();
        }
    }
    println!("{}",ratio);
}
