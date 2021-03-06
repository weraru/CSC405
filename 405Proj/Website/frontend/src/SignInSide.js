import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import {Link} from 'react-router-dom';
import { useState } from 'react';
import Auth from './Auth';
import FailLogin from './FailLogin';


function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}


const useStyles = makeStyles(theme => ({
  root: {
    height: '100vh',
  },
  image: {
    backgroundImage: '',
    backgroundRepeat: 'no-repeat',
    backgroundColor:
      theme.palette.type === 'dark' ? theme.palette.grey[900] : theme.palette.grey[50],
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

function CallAPI(signin){
    //console.log(JSON.stringify(signin));
    // POST request using fetch inside useEffect React hook
    
    //return(result);
    // empty dependency array means this effect will only run once (like componentDidMount in classes)
}

export default function SignInSide(props) {
  const classes = useStyles();
  const [ signin, setSignin ] = useState({username: '', password: ''});  
  const [code, setResult] = useState('');
  const  { name, pass } = '';
  const [showIndiv, setShowIndiv] = React.useState(false);

  const changeHandler = (e) => {
    
    setSignin({...signin, [e.target.name]: e.target.value});


  }

  const submitHandler = e => {
    e.preventDefault()
  
  /*  var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    //myHeaders.append("Content-Type", "application/json");
    
    var raw = JSON.stringify({"username":signin.username,"password":signin.password});
    
    var requestOptions = {
      method: 'POST',
      mode: 'cors',
      headers: myHeaders,
      body: raw,
      redirect: 'follow',
    };
    
    fetch("https://162.236.218.100:5005/login", requestOptions)
      .then(response => response.json())
      .then(result => 
        {if (Auth.login(() => {props.history.push("/EmployeePage")}, result) == "-1")
        setShowIndiv(true);
      });*/
      Auth.login(() => {props.history.push("/EmployeePage")});
};
  let IndivClose = () => {
    setShowIndiv(false);
  }
 

  //console.log(signin);
  return (
    <div>
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <Grid item xs={false} sm={4} md={7} className={classes.image} />
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <form 
            className={classes.form} noValidate
            onSubmit={submitHandler}
          >
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="User Name"
              name="username"
              value = {signin.username}
              onChange = {changeHandler}
              autoComplete="username"
              autoFocus
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              value = {signin.password}
              onChange = {changeHandler}
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
              <Link to ='/forgotpassword'>
            <li>Forgot Password?</li>
              </Link>
              </Grid>
              <Grid item>
              <Link to ='/signup'>
            <li>Don't have an account? Sign Up</li>
              </Link>
              </Grid>
            </Grid>
            <Box mt={5}>
              <Copyright />
            </Box>
          </form>
        </div>
      </Grid>
    </Grid>
        <FailLogin 
        show = {showIndiv}
        onHide = {IndivClose} 
      />
      </div>
  );
}