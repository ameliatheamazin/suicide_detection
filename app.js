
const express=require("express"); 
const router=express.Router()
const cookieParser=require('cookie-parser')
//const session=require('express-session')
const bodyParser=require('body-parser')
const app=express(); 

app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json())
app.use(cookieParser('secret'))

app.set('view engine','ejs')
//setting up the routes
app.get('/',(req,res)=>{
    console.log('here')

    //sending HTTP codes
    //res.json({message:"Success"})
    res.render('index')

})

//use routers from the route file
//const mainRouter=require('./routes/route')
//app.use('/home',mainRouter)

app.listen(3000)