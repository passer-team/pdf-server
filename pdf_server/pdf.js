/**
 * @author Daryl Xu <ziqiang_xu@qq.com>
 * convert html to pdf
 */
// https://pptr.dev/
const path = require('path');
const puppeteer = require('puppeteer');

const args = process.argv.slice(2);

console.log(`HTML resource：${args[0]}，PDF output path：${args[1]}`);

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  // await page.goto('https://www.baidu.com', {waitUntil: 'networkidle2'});
  console.log('Load the HTML')
  await page.goto(
    `file://${path.resolve(args[0])}`,
    { timeout: 0,  waitUntil: 'networkidle2' });
  
  console.log('Start to render HTML to PDF')
  await page.pdf({
    path: args[1],
    format: 'A4',
    printBackground: true
  });
  await browser.close();
  console.log('Render finished and close the browser!')
})();
