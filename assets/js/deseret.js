
/* borrowed from http://www.keyboardninja.eu/webdevelopment/a-simple-search-with-angularjs-and-php */
var app = angular.module("DeseretTranslatorApp", []);

app.controller("TranslationController", ['$scope', '$http', '$sce', function($scope, $http, $sce) {
	$scope.url = '/json/translation'; // The url of our search
		
	// The function that will be executed on button click (ng-click="translate()")
	$scope.translate = function() {
		
		// Create the http post request
		// the data holds the keywords
		// The request is a JSON request.
		$http.post($scope.url, { "english" : $scope.english}).
		success(function(data, status) {
			$scope.status = status;
			$scope.data = data;
			$scope.deseret = $sce.trustAsHtml(data.deseret); // Show result from server in our <pre></pre> element
		})
		.
		error(function(data, status) {
			$scope.data = data || "Request failed";
			$scope.status = status;			
		});
	};
}])
