import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import App from 'app/App';
import rootReducer from 'redux/reducers';

const enhancers = compose(applyMiddleware(thunk));
const store = createStore(rootReducer, enhancers);

const container = document.getElementById('root');
const root = createRoot(container);
root.render(
    <Provider store={store}>
        <App />
    </Provider>
);

export default store;
