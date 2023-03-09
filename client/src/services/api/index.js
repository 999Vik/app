const defaultImportError = () => {
    console.error(
        'API imported as default from services/api instead of using destructuring. Import with this import { X } from ...'
    );
};

export default defaultImportError;
