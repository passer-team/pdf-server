/**
 * @author Daryl Xu <xuziqiang@zyheal.com>
 * convert html to pdf
 */
// https://pptr.dev/
const path = require('path');
const puppeteer = require('puppeteer');

const args = process.argv.slice(2);

console.log(`${args[0]} ${args[1]}`);

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  // await page.goto('https://www.baidu.com', {waitUntil: 'networkidle2'});
  // await page.goto('file:///home/ziqiang_xu/Seafile/LiverDataExample(12)/selected/01190626V001/report/resources/report.html', {waitUntil: 'networkidle2'});
  await page.goto(
    `file://${path.resolve(args[0])}`,
    { waitUntil: 'networkidle2' });
  await page.pdf({
    // path: '/home/ziqiang_xu/Seafile/LiverDataExample(12)/selected/01190626V001/report/report.pdf', 
    path: args[1],
    format: 'A4',
    printBackground: true
  });

  await browser.close();
})();
