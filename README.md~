## Prerequisites
Here are some depenencies :
- git
- nodejs
- nodejs-legacy (not always needed)
- npm
- grunt-cli
- bower

On ubuntu-like distributions, you can install those dependencies by running :
```bash
sudo apt-get install git nodejs npm nodejs-legacy
sudo npm install -g grunt-cli
sudo npm install -g bower
```

## Installing and running the environement

Enter the `bootstrap-hbp-app` folder :
```bash
cd bootstrap-hbp-app
```
Generate your project template by running :
```bash
./init.py <Your application name> <Path to your application logo>
```
    
Run the application :

```bash
grunt serve
```

After each changes you should be able to see your current code running by refreshing your browser page.

## Getting started

Your application folder is `app/scripts/app/<appName>/`. Open it to start working.
Do not create/edit/delete any file outside of this directory. Also, you should not edit the following files except if you know what you are doing : `index.html` and `<appName>.module.js`.
Your app can be made of HTML, CSS, Javascript, JQuery and/or AngularJS.
Feel free to create folders in your working directory, add some data-mock files, and so on.

Create your first app :

- Let's edit our HTML view in `<appName>.html` :

    ```html
    <h1>An example</h1>
    <p>It works ! </p>
    ```

- Let's add CSS in the `css/style.css` file to make it look nicer :
    ```html
    <link rel="stylesheet" type="text/css" href="scripts/app/<appName>/css/style.css" />

    <div class=myClass>
        <h1>An example</h1>
        <p>If this div background is gray and beautiful, you should be happy !</p>
    </div>
    ```
    ```css
    .myClass {
        background-color: rgba(100,100,100,0.5);
        border-radius: 25px;
        padding: 20px;
    }
    ```

- Let's add some Javascript/JQuery code in the `js/script.js` file :
    ```html
    <link rel="stylesheet" type="text/css" href="scripts/app/<appName>/css/style.css" />
    <script src="scripts/app/<appName>/js/script.js"></script>

    <div class=myClass>
        <h1>An example</h1>
        <p>If this div background is gray and beautiful, you should be happy !</p>
        <button id="testButton" type="button">Click Me!</button> 
    </div>
    ```
    ```javascript
    $(document).read(function() {
        $( "#testButton" ).click(function() {
            alert( "JS and JQuery are working ! " );
        });
    });
    ```


- Let's add a logo or an image in the `images` folder and use it in our HTML view :
    ```html
    <link rel="stylesheet" type="text/css" href="scripts/app/<appName>/css/style.css" />
    <script src="scripts/app/<appName>/js/script.js"></script>
    
    <div class=myClass>
        <img class="logo" src="scripts/app/<appName>/images/logo.png" alt="application logo"></img>
        <h1>An example</h1>
        <p>If this div background is gray and beautiful, you should be happy !</p>
        <button id="testButton" type="button">Click Me!</button> 
    </div>
    ```

- Let's make it look a bit nicer:
    ```css
    .myClass {
        background-color: rgba(100,100,100,0.5);
        border-radius: 25px;
        padding: 20px;
    }
    .logo {
        width: 80px;
        height: 80px;
        float: right;
    }
    ```

- Let's add some AngularJS in our view and let's use our controller `<appName>.controller.js` too :
    ```html
    <link rel="stylesheet" type="text/css" href="scripts/app/<appName>/css/style.css" />
    <script src="scripts/app/<appName>/js/script.js"></script>
    
    <div class=myClass ng-controller="<appName>Controller">
        <img class="logo" src="scripts/app/<appName>/images/logo.png" alt="application logo"></img>
        <h1>An example</h1>
        <p>If this div background is gray and beautiful, you should be happy !</p>
        <input type="text" ng-model="name" placeholder="Enter a name here">
        <p>Hello {{name}}! AngularJS is working !</p>
        <button id="testButton" type="button">Test</button>
        <button id="resetButton" type="button" ng-click='resetName()'>Reset</button>
    </div>
    ```
    ```javascript
    angular.module('chuvApp.<appName>').controller('<appName>Controller',['$scope',
      function($scope) {
        $scope.resetName = function() {
          $scope.name = ''
        }
    }]);
    ```
- Let's try our first app :
    ```html
    <link rel="stylesheet" type="text/css" href="scripts/app/<appName>/css/style.css" />
    <script src="scripts/app/<appName>/js/script.js"></script>
    
    <div class=myClass ng-controller="<appName>Controller">
        <img class="logo" src="scripts/app/<appName>/images/logo.png" alt="application logo"></img>
        <h1>An example</h1>
        <p>If this div background is gray and beautiful, you should be happy !</p>
        <input type="text" ng-model="name" placeholder="Enter a name here">
        <p>Hello {{name}}! AngularJS is working !</p>
        <button id="testButton" type="button">Test</button>
        <button id="resetButton" type="button" ng-click='resetName()'>Reset</button>
    </div>
    ```
    ```javascript
    angular.module('chuvApp.<appName>').controller('<appName>Controller',['$scope',
      function($scope) {
        $scope.resetName = function() {
          $scope.name = ''
        }
    }]);
    ```
    ```css
    .myClass {
	    background-color: rgba(100,100,100,0.5);
	    border-radius: 25px;
	    padding: 20px;
    }
    .logo {
	    width: 80px;
	    height: 80px;
	    float: right;
    }
    ```
    ```javascript
    $(document).ready(function() {
        $( "#testButton" ).click(function() {
            alert( "JS and JQuery are working ! " );
        });
    });
    ```  
