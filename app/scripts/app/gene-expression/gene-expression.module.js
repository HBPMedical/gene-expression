
angular.module('chuvApp.gene-expression', ['ngResource','ui.router'])
.config(['$stateProvider', function ($stateProvider) {
    $stateProvider
    .state('myapp', {
        url: '/hbpapps/gene-expression',
        templateUrl: 'scripts/app/gene-expression/index.html',
        controller:'gene-expressionController'
    })
}]);
