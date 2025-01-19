class Anim{
    constructor(n, a) {
        this.n = n;
        this.a = a;
    };
    
    speak() {
        console.log("This animal makes a sound.");
    };
}

class Cat extends Anim {
    speak () {
        console.log("Meow!");
    };
};

class snake extends Animal {
    speak () {
        console.log("SSSSSSSSSSSSSSSSSSSSS!");
    }
};