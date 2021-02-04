function are_equal<T, U>(a: T, b: U): boolean {
    return +a == +b;
}
console.log(are_equal<number,number>(10, 10.0));