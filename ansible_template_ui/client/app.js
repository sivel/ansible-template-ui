(function() {
    ngApp = angular.module('ngApp', ['blockUI', 'ui.bootstrap']);

    ngApp.controller('mainController', [
        '$scope',
        '$http',
        '$sce',
        function($scope, $http, $sce) {
            $scope.variables = '';
            $scope.template = '';
            $scope.rendered = '';
            $scope.error = '';

            $scope.templateExample = '{{ foo }}';

            $scope.sample = function() {
                $scope.variables = 'foo: bar';
                $scope.template = $scope.templateExample;
                $scope.render();
            }

            $scope.render = function(tag) {
                var tag = tag || 'latest';
                $scope.rendered = '';
                $scope.error = '';
                $http.post(
                    'render',
                    {
                        variables: $scope.variables,
                        template: $scope.template,
                        tag: tag,
                    }
                ).then(
                    function(response) {
                        console.log(response);
                        $scope.rendered = response.data.content;
                        console.log($scope.rendered);
                    },
                    function(response) {
                        console.log(response);
                        $scope.error = response.data.error;
                    }
                )
            }
        }
    ]);
})();
