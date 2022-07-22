
const needle=require('needle')
const config=require('dotenv').config()
const TOKEN=process.env.TWITTER_BEARER_TOKEN

const rulesURL='https://api.twitter.com/2/tweets/search/stream/rules'
const streamURL='https://api.twitter.com/2/tweets/search/stream?tweet.fields=public_metrics'

const rules=[{value:'i am suicidal'}]

const express=require("express"); 
const axios = require('axios')
const router=express.Router()
const cookieParser=require('cookie-parser')
//const session=require('express-session')
const bodyParser=require('body-parser')
const app=express(); 

// app.use(bodyParser.urlencoded({extended:false}))
// app.use(bodyParser.json())
// app.use(cookieParser('secret'))

app.set('view engine','ejs')
//setting up the routes
app.get('/',(req,res)=>{
    console.log('here')

    //sending HTTP codes
    //res.json({message:"Success"})
    res.render('../templates/index')

})

app.post('/', function(req, res) {
    axios.post('http://127.0.0.1:5000/',{ tweet:req.params.tweet}).then(
        (response) => {
            var result = response.data;
            console.log(result);
        },
        (error) => {
            console.log(error);
        }
    );

});



// //Get stream rules
// async function getRules(){
//     const response=await needle('get',rulesURL,{
//         headers:{
//             Authorization:`Bearer ${TOKEN}`
//         },
//     })
//     //onsole.log(response.body)
//     return response.body
// }

// //Set stream rules
// async function setRules(){
//     const data={
//         add: rules
//     }
//     const response=await needle('post',rulesURL,data, {
//         headers:{
//             'content-type':'application/json',
//             Authorization:`Bearer ${TOKEN}`
//         },
//     })
//     //console.log(response.body)
//     return response.body
// }

// //Delete stream rules
// async function deleteRules(rules){
//     if(!Array.isArray(rules.data)){
//         return null
//     }
//     const ids=rules.data.map((rule)=>rule.id) //for each rule, extract the id
//     const data={
//         delete:{
//             ids:ids
//         }
//     }
//     const response=await needle('post',rulesURL,data, {
//         headers:{
//             'content-type':'application/json',
//             Authorization:`Bearer ${TOKEN}`
//         },
//     })
//     //console.log(response.body)
//     return response.body
// }

// function streamTweets(){
//     const stream=needle.get(streamURL, {
//         headers:{
//             Authorization:`Bearer ${TOKEN}`
//         }
//     })

//     stream.on('data',(data)=>{
//         try{
//             console.log(data)
//             // console.log(data.toString('utf8'))
//             const json=JSON.parse(data)
//             console.log(json)
//         }catch(error){
//             console.log(error)
//         }
//     })
// }

// (async () =>{
//     let currentRules
//     try{
//         //get all prev stream rules
//         currentRules=await getRules()
//         //delete all prev stream rules
//         await deleteRules(currentRules)
//         //set new rules
//         await setRules()
        
//     }catch(error){
//         console.log(error)
//         process.exit(1)
//     }

//     streamTweets()
// })()
//use routers from the route file
//const mainRouter=require('./routes/route')
//app.use('/home',mainRouter)

app.listen(3000,function(){
    console.log(`server started successfully`)
})
