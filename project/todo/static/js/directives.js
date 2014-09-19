(function(){
    app = angular.module('todo-directives', []);

    app.directive("autosaveForm", function($timeout,$location,Post) {
        var promise;
        return {
            restrict: "A",
            controller:function($scope){
                $scope.post = {};
                $scope.save = function(){
                    console.log(promise);
                    $timeout.cancel(promise);
                    if(typeof $scope.post.put === 'function'){
                        $scope.post.put().then(function() {
                            return $location.path('/post');
                        });
                    }
                    else{
                        Post.store($scope.post).then(
                            function(data) {
                                return $location.path('/post');
                            },
                            function error(reason) {
                                throw new Error(reason);
                            }
                        );
                    }
                };

            },
            link: function (scope, element, attrs) {
                scope.$watch('form.$valid', function(validity) {
                    element.find('#status').removeClass('btn-success');
                    element.find('#status').addClass('btn-danger');
                    if(validity){
                        Post.store(scope.post).then(
                            function(data) {
                                element.find('#status').removeClass('btn-danger');
                                element.find('#status').addClass('btn-success');
                                scope.post = Post.copy(data);
                                _autosave();
                            },
                            function error(reason) {
                                throw new Error(reason);
                            }
                        );
                    }
                })
                function _autosave(){
                        scope.post.put().then(
                        function() {
                            promise = $timeout(_autosave, 2000);
                        },
                        function error(reason) {
                            throw new Error(reason);
                        }
                    );
                }
            }
        }
    })

    app.directive('addItemAction', function(){
    return {
        'restrict': 'E',
        'template': '<div class="col-md-12">' +
                        '<fieldset class="form-group pull-right">' +
                            '<button type="submit" class="btn btn-primary btn-default btn-block">Add</button>' +
                        '</fieldset>' +
                    '</div>'
        }
    });

    app.directive('deleteItemAction', function(){
        return {
            'restrict': 'E',
            'template': '<div class="col-md-12">' +
                            '<fieldset class="form-group pull-right">' +
                                '<button type="submit" class="btn btn-danger btn-default btn-block">Delete</button>' +
                            '</fieldset>' +
                        '</div>'
        }
    });

    app.directive('itemDirective', function(){
        return {
            'restrict': 'E',
            'templateUrl': '/static/item.html'
            }
        });
})();