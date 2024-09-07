fn test() -> i32 {
    let mut x = 1000;

    if { let y = 400;
         if y < 100 { true } else { false } } 
    { 
        x += 100;
    }

    if true { x += 10; }
    else { x += 1; }

    x
}

fn main() {
    let x = test();
    println!("{x}");
}