class Auth {
    constructor(){
        this.athenticated = false;
    }
}

login(cb, data){

    
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