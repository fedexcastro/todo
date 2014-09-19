(function () {
    app = angular.module('todo', ['todo-directives']);
    app.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[{');
      $interpolateProvider.endSymbol('}]}');
    });


    app.controller('ItemController', ['$scope', '$http', function($scope, $http){
        $scope.form = {
            state: {},
            data: {},
            action: 'delete'
        };

        $scope.init = function(item, action) {
            $scope.form.data = item;
            $scope.form.action = action;
        };

        $scope.delete = function() {
            var itemID = $scope.form.data.id;
            $http.delete('/api/v1/item/'+itemID+'?format=json').success(function(data){
                $('#item-'+itemID).parent().remove();
            });
        };

        $scope.update = function() {
            $http.put('/api/v1/item/?format=json', $scope.form.data).success(function(data){
                console.log("Updated!");
            })
        };

        $scope.create = function() {
            $http.post('/api/v1/item/?format=json', $scope.form.data).success(function(data){
                var html = '';
                $http.get('/static/item.html').success(function(data){
                    html = data;
                    $scope.$parent.items.push(html);
                    $compile($scope.$parent.items.contents)($scope.form.data);
                });
            })
        };

        $scope.submit = function () {
            if ($scope.form.action === 'add') {
                $scope.create();
            } else if ($scope.form.action==='delete') {
                $scope.delete();
            } else {
                $scope.update();
            };
        };
    }]);

    app.controller('ListController', ['$scope', '$http', function($scope, $http){
        $scope.items = [];

        $http.get('/api/v1/item/?format=json').success(function(data){
            $scope.items = data.objects;
        });
    }]);

})();