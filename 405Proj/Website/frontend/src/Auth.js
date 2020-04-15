class Auth {
    constructor(){
        this.athenticated = false;
    }


login(cb, data){
    console.log(data.token);
    if (data.token){
        
        this.authenticated = true;
        cb();
    }
    
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