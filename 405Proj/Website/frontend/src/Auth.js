class Auth {
    constructor(){
        this.athenticated = false;
    }


login(cb, data){
    //if(data == "-1" || data == null || data == "wrong format" ){
        
    //    return ("-1");
    //}
        this.authenticated = true;
        cb();
    
}

logout(cb){
    this.authenticated = false;
    cb();
}

isAuthenticated(){
    return this.authenticated;
}
}
export default new Auth();