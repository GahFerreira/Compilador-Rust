fn f() -> i32 
{
    let mut x : i32;
    x = 15 + 0b1 + 0o7 + 0xF;
    x = 15 + 0o7 * 0xF / 1 % 0b1;
    x = 15 + 0b1 + 0o7 + 0xF;
    x = x + (15 + 0b1) * (15 - 0b1);

    let mut y : bool;
    y = (1 < 2 && 2 < 3) <= (2 > 3);
    y = !y || (1 != 0) >= (1 == 0);

    if y
    {
        let z : bool;

        z = true;

        y = y == z;
    }

    while x > 0
    {
        if x < 0
        {
            x = 0 - x;
        }

        x = x - 1;
    }

    if x == 0
    {
        x = 10;
    }

    else
    {
        x = -10 + g(0b1, 0o5, 0xAA);
    }

    let arr: [i32 ; 3];
    
    arr = [15, 20, 30];
    x = x + arr[2];

    x
}

fn g(a : i32, b : i32, c : i32) -> i32 { a + b * c }

fn main() -> () {
    println!("{}", f());
}