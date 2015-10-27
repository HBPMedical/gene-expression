#!/usr/bin/env python

import argparse, os, subprocess


def getArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('appName', help='Application name')
	parser.add_argument('logo', help='Application logo')
	return parser.parse_args()


def writeFile(fileName, content):
	try:
		f = open(fileName, 'w')
		f.write(content)
		f.close()
	except IOError:
		print 'writeFile : Cannot write in '+fileName+' file ! '

def findAndAppend(fileName, pattern, incl):
	try:
		content = ''
		f = open(fileName, 'r')
		for line in f:
			content += line
			if pattern in line:
				content += incl
		f.close()
		writeFile(fileName, content)
	except IOError:
		print 'findAndAppend : Cannot read '+fileName+' file ! '


def findAndPrepend(fileName, pattern, incl):
	try:
		content = ''
		f = open(fileName, 'r')
		for line in f:
			if pattern in line:
				content += incl
			content += line
		f.close()
		writeFile(fileName, content)
	except IOError:
		print 'findAndPrepend : Cannot read the file '+fileName+' ! '


def fileContains(fileName, pattern):
	try:
		f = open(fileName, 'r')
		for line in f:
			if pattern in line:
				f.close()
				return True
		f.close()
		return False
	except IOError:
		print 'fileContains : Cannot read '+fileName+' file ! '


def replaceContent(fileName, pattern, replacement):
	try:
		f = open(fileName, 'r')
		content = f.read()
		f.close()
		newContent = content.replace(pattern, replacement)
		writeFile(fileName, newContent)
	except IOError:
		print 'replaceContent : Cannot read '+fileName+' file ! '


def main():
	# Get arguments
	args = getArgs()

	APP_ID = args.appName.lower()
	APP_PATH = os.path.join('app/scripts/app/', APP_ID)

	# Install node and bower dependencies
	subprocess.call(['sudo', 'npm', 'install'])
	subprocess.call(['bower', 'install'])

	# Create application folders
	subprocess.call(['mkdir', APP_PATH])
	subprocess.call(['mkdir', os.path.join(APP_PATH, 'css')])
	subprocess.call(['mkdir', os.path.join(APP_PATH, 'js')])
	subprocess.call(['mkdir', os.path.join(APP_PATH, 'images')])

	# Add files
	subprocess.call(['touch', os.path.join(APP_PATH, 'index.html')])
	subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.html')])
	subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.module.js')])
	subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.controller.js')])
	subprocess.call(['touch', os.path.join(APP_PATH, 'css', 'style.css')])
	subprocess.call(['touch', os.path.join(APP_PATH, 'js', 'script.js')])
	subprocess.call(['cp', args.logo, os.path.join(APP_PATH, 'images', 'logo.png')])

	# Set up project
	indexCode = '''
<div class="container-fluid mt" ng-include=" 'scripts/app/'''+APP_ID+'/'+APP_ID+'''.html' ">
</div>
'''
	viewCode = '''
<link rel="stylesheet" type="text/css" href="scripts/app/'''+APP_ID+'''/css/style.css" />
<script src="scripts/app/'''+APP_ID+'''/js/script.js"></script>

<div ng-controller="'''+APP_ID+'''Controller">
  <h1>This is your view</h1>
</div>
'''
	moduleCode = '''
angular.module('chuvApp.'''+APP_ID+'''\', ['ngResource','ui.router'])
.config(['$stateProvider', function ($stateProvider) {
    $stateProvider
    .state(\''''+APP_ID+'''\', {
        url: '/hbpapps/'''+APP_ID+'''',
        templateUrl: 'scripts/app/'''+APP_ID+'''/index.html',
        controller:\''''+APP_ID+'''Controller'
    })
}]);
'''
	controllerCode = '''
angular.module('chuvApp.'''+APP_ID+'''\').controller(\''''+APP_ID+'''Controller',[
  function(){
}]);
'''
	writeFile(os.path.join(APP_PATH, 'index.html'), indexCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.html'), viewCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.module.js'), moduleCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.controller.js'), controllerCode)


	# Set up app URL in `Gruntfile.js`
	replaceContent('./Gruntfile.js', 'target: \'http://localhost:9002/#/hbpapps/myapp\'', 'target: \'http://localhost:9002/#/hbpapps/'+APP_ID+'\'')

	# Add module in `app.js`
	path = './app/scripts/app/app.js'
	if fileContains(path, '\'chuvApp.'+APP_ID+'\''):
		print 'The module '+'\'chuvApp.'+APP_ID+'\'seems to already exist in the `app.js` file ! '
	else:
		findAndAppend(path, '//ui modules', '    \'chuvApp.'+APP_ID+'\',\n')	

	# Include module and controller to the main project
	path = './app/index.html'
	inclStr = '\n<!-- JS inclusions for external app "'+APP_ID+'" -->\n'
	inclStr += '<script src="scripts/app/'+APP_ID+'/'+APP_ID+'.module.js"></script>\n'
	inclStr += '<script src="scripts/app/'+APP_ID+'/'+APP_ID+'.controller.js"></script>\n'
	if fileContains(path, inclStr):
		print 'The Javascript inclusions for this app seem to already exist in the `'+path+'` file ! '
	else:
		findAndPrepend(path, '</body>', inclStr)

	# Show welcome message
	print 'To run your application, use `grunt serve` ! '


if __name__ == '__main__':
	main()