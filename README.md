# carepy - React and Python Flask - Full Stack application

carepy is the fastest way to spin up a Full Stack application (React + Flask) with [Cucumber](https://docs.cucumber.io/guides/10-minute-tutorial/) and [Behave](https://behave.readthedocs.io/en/latest/) BDD testing 

## Prerequisites

* [NodeJS (v11.2.0)](https://nodejs.org/en/)
* [Python (v3.7.2)](https://www.python.org/)
* [Pipenv (v2018.11.26)](https://pipenv.readthedocs.io/en/latest/)

Note: To quickly install Pipenv execute the command ```pip install --user pipenv```

## QuickStart
1. Navigate to the Full_Stack directory
2. Open terminal of choice in the Full_Stack directory
3. Install your dependencies with ```npm run install:all```
4. Execute your Cucumber tests with ```npm run test:all```
5. Run your application with ```npm run dev:all```
6. Ready to Code!

## FAQ

Q: Can I use Node on the backend instead of Python?

A: Careen.js is the fastest way to spin up a Node + React application with BDD. It is located at https://github.com/NguyenAndrew/careen

---

Q: What technologies are used on the back end?

A: Python + Flask + Behave

---

Q: What technologies are used on the front end?

A: Node + Enzyme + Express + Cucumber is used for testing. The application uses React (Made with [Create React App](https://facebook.github.io/create-react-app/)) and Axios.

---

Q: Can I see my changes live while developing? 

A: Yes! ```npm run dev:all``` uses Create React App to watch changes on the React application and Flask debug mode to watch changes on the back end server.

---

Q: What does ```npm run test:watch:all``` do in the Full_Stack directory?

A: This command allows for quick continuous BDD/TDD. To use, open up a second terminal/shell/command prompt, and execute this command there. When changes on src or test are made and saved, the tests will automatically re-run without having to reload the transpiler (Babel) for the React Application, which is a feature achieved through [babel-watch](https://github.com/kmagiera/babel-watch). The Python Flask application uses [Nodemon](https://nodemon.io/) to watch changes for tests in the python application.