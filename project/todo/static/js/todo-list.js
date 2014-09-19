(function () {
    app = angular.module('todo-list', [])
    app.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[{');
      $interpolateProvider.endSymbol('}]}');
    });

    app.directive('todoList', function(){
        return {
            'restrict': 'E',
            'templateUrl': '/static/templates/list.html',
            'controller': ['$http', function($http) {
                this.list_items = [];
                $http.get('/api/v1/item/?format=json').success(function(data){
                    this.list_items = data.objects;
                });

                this.getItems = function(){
                    return this.list_items;
                };

            }],
            'controllerAs': 'list'
        }
    });


})();