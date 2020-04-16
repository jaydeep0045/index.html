const typewriter = function(txtelement,words,wait = 3000)
{
    this.txtelement = txtelement;
    this.words = words;
    this.txt = '';
    this.wordindex = 0;
    this.wait = parseInt(wait,10);
    this.type();
    this.isDeleting = false;

}

//type method
typewriter.prototype.type = function()
{
   //console.log("helllo");
   //current index of word
   const current =this.wordindex % this.words.length;
   //get full text of current word
   const fulltext = this.words[current];
   console.log(fulltext);

   //check is deleting
   if(this.isDeleting)
   {
        //remove char
        this.txt = fulltext.substring(0,this.txt.length-1);
   }
   else
   {
        //add char
        this.txt = fulltext.substring(0,this.txt.length+1);
   }
   //insert txt into element
   this.txtelement.innerHTML = '<span>'+this.txt+'</span>';
   //type speed
   let typespeed = 300;

   if(this.isDeleting)
   {
        typespeed /= 2;
   }

   //if word is complet
   if(!this.isDeleting && this.txt === fulltext)
   {
       //make pause at end 
        typespeed = this.wait;
        //set delete to true
        this.isDeleting =true;
   }
   else if(this.isDeleting && this.txt === '')
   {
    this.isDeleting =false;
    //move to next word
    this.wordindex++;
    //pause before start typing
    typespeed = 500;
   }
    setTimeout(() => this.type(),typespeed)
}

//init on DOM load
document.addEventListener('DOMContentLoaded',init);

//Init app
function init()
{
    const txtelement = document.querySelector('.type');
    const words = JSON.parse(txtelement.getAttribute('data-words'));
    const wait = txtelement.getAttribute('data-wait');

    //Init typewriter
    new typewriter(txtelement,words,wait)
} 