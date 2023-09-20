"module"

console.log("started tests")

function test() {
    console.log("test function called")
}

function test2(arg1) {
    console.log("test2 function called with arg1: " + arg1)
}

export { test, test2 }