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

            $scope.raw = false;

            $scope.sample = function() {
                $scope.variables = 'foo: bar';
                $scope.template = $scope.templateExample;
                $scope.raw = false;
                $scope.render();
            }

            $scope.render = function(tag) {
                var tag = tag || 'latest';
                if ($scope.raw) {
                    var template = '{{ ' + $scope.template + ' }}';
                } else {
                    var template = $scope.template;
                }
                $scope.rendered = '';
                $scope.error = '';
                $http.post(
                    'render',
                    {
                        variables: $scope.variables,
                        template: template,
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
