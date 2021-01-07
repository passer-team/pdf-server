const path = require("path");

const args = process.argv.slice(2);

console.log(`the arguments: ${args[0]} ${args[1]}`);

relative_path = 'tests/test_pytest.py';
console.log('absolute path: ', path.resolve(relative_path)); 


relative_path = '/home/tests/test_pytest.py';
console.log('absolute path: ', path.resolve(relative_path)); 
