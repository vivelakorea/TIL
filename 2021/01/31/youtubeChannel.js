const axios = require('axios');

const channelId = 'UCUj6rrhMTR9pipbAWBAMvUQ';
// 채널 링크가 https://www.youtube.com/channel/UCmbGE7Y2ov7pTBuUrkXgtTQ 이런식이면 channelId = 'UCmbGE7Y2ov7pTBuUrkXgtTQ'
// 채널 링크가 https://www.youtube.com/user/zilioner83 이런식이면 username= 'zilioner83'

const util = require('util');

const optionParams = {
    part: 'statistics',
    id: channelId, // 혹은 forUsername: username
    key: '<youtube API key>',
    maxResults: 1,
};

let url = 'https://www.googleapis.com/youtube/v3/channels?';
for (let option in optionParams) {
    url += `${option}=${optionParams[option]}&`;
}
url = url.slice(0, -1);

console.log(url);


(async () => {
    try {
        const res = await axios.get(url);
        console.log(util.inspect(res.data.items[0], {showHidden: false, depth: 5}))
    } catch (err) {
        console.error(err);
    }
})();