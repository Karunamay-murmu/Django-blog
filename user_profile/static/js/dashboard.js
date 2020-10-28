import { Spinner, detectMutate } from '../../../static/js/spinner.js';

/**
 * show the spinner until the dashboard is loaded
 * */
const loader = new Spinner()
loader.show()
detectMutate(loader)

/**
 * toggle sidebar on mobile device
 */


