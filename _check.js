
(function(){
  var q=document.getElementById('q'),
      cnt=document.getElementById('count'),
      clr=document.getElementById('clear'),
      nores=document.getElementById('noresult'),
      cards=[].slice.call(document.querySelectorAll('.card')),
      cats=[].slice.call(document.querySelectorAll('.cat')),
      total=cards.length;
  function norm(s){return s.toLowerCase().replace(/ä/g,'ae').replace(/ö/g,'oe').replace(/ü/g,'ue').replace(/ß/g,'ss').replace(/[„“–]/g,'');}
  function run(){
    var terms=norm(q.value.trim()).split(/\s+/).filter(Boolean);
    var shown=0;
    cards.forEach(function(c){
      var hay=c.getAttribute('data-s');
      var ok=terms.every(function(t){return hay.indexOf(t)>-1;});
      c.style.display=ok?'':'none';
      if(ok)shown++;
    });
    cats.forEach(function(sec){
      var any=sec.querySelector('.card:not([style*="none"])');
      sec.style.display=any?'':'none';
    });
    nores.style.display=shown?'none':'block';
    cnt.textContent = terms.length ? (shown+' von '+total+' Beiträgen') : (total+' Beiträge');
  }
  q.addEventListener('input',run);
  clr.addEventListener('click',function(){q.value='';run();q.focus();});
  run();
})();
