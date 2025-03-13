import * as readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function input(pergunta: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(pergunta, (resposta) => {
      resolve(resposta);
    });
  });
}

async function main() {
  const first_number:number = parseInt(await input(''));
  const second_number:number = parseInt(await input('')); 

  console.log(`X = ${first_number + second_number}`);

  rl.close();
}

main();