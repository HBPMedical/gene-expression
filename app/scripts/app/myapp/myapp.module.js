angular.module('chuvApp.myapp', ['ngResource','ui.router'])
    .config(['$stateProvider', function ($stateProvider) {
        $stateProvider
        .state('myapp', {
            url: '/hbpapps/myapp',
            templateUrl: 'scripts/app/myapp/myapp.html',
            controller:'MyAppController'
        })
    }]);
