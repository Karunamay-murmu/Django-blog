export class Spinner{show(){const body=document.querySelector('.body')
const textarea=document.querySelector('#id_body')
const container=document.createElement('div')
const spinner=document.createElement('div')
spinner.id='spinner'
container.id='loader-container'
container.appendChild(spinner)
body.insertBefore(container,textarea)}
hide(){const container=document.querySelector('#loader-container')
container.remove()}}
export function detectMutate(loader){const editor=document.querySelector('.body')
const observer=new MutationObserver(function(mutationRecord){for(let record of mutationRecord){if(record.type==='childList'){loader.hide();}}})
observer.observe(editor,{childList:true,attributes:true})}