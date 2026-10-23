(function(){
  var box = document.getElementById('next-unread-box');
  if(!box) return;
  var here = location.pathname.split('/').pop();

  fetch('categories.json', {cache:'no-cache'}).then(function(r){
    if(!r.ok) throw new Error('categories.json nicht verfuegbar');
    return r.json();
  }).then(function(data){
    var cat = null, list = null;
    for(var k in data){
      if(data[k].some(function(it){ return it.href === here; })){
        cat = k; list = data[k]; break;
      }
    }
    if(!list) return;

    var read;
    try{ read = JSON.parse(localStorage.getItem('df_read')||'[]'); }catch(e){ read = []; }
    var readSet = {};
    read.forEach(function(h){ readSet[h]=true; });

    var startIdx = list.findIndex(function(it){ return it.href === here; });
    var next = null;
    for(var i=1;i<=list.length;i++){
      var idx = (startIdx+i) % list.length;
      var cand = list[idx];
      if(cand.href === here) continue;
      if(!readSet[cand.href]){ next = cand; break; }
    }

    var labelStyle = "font-family:'Courier New',monospace;font-size:0.7rem;letter-spacing:0.08em;text-transform:uppercase;color:#8a8a92;margin-bottom:0.6rem;";
    var linkStyle = "color:#e8c547;text-decoration:none;font-family:Georgia,'Times New Roman',serif;font-size:1.05rem;";
    var subStyle = "display:block;margin-top:0.6rem;";

    if(next){
      box.innerHTML =
        '<div style="'+labelStyle+'">Weiterlesen in dieser Rubrik</div>' +
        '<a href="'+next.href+'" style="'+linkStyle+'">&rarr; '+next.title+'</a>' +
        '<a href="themen.html" style="'+subStyle+'font-family:\'Courier New\',monospace;font-size:0.68rem;color:#6b6b75;">Alle Rubriken im Archiv</a>';
    } else {
      box.innerHTML =
        '<div style="'+labelStyle+'">&#10003; Rubrik vollständig gelesen</div>' +
        '<a href="themen.html" style="'+linkStyle+'">&rarr; Nächste Rubrik im Archiv wählen</a>';
    }
    box.style.display = 'block';
  }).catch(function(){ /* still, Seite bleibt unveraendert */ });
})();
