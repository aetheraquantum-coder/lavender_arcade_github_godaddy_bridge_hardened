(function(){
  var root=document;
  var age=root.getElementById('ageFilter');
  var mode=root.getElementById('modeFilter');
  var region=root.getElementById('regionFilter');
  var search=root.getElementById('searchFilter');
  var cards=root.getElementsByClassName('game-card');
  var msg=root.getElementById('countMessage');

  function ageRank(v){
    var map={'u13':0,'13':1,'17':2,'18':3};
    return map.hasOwnProperty(v)?map[v]:99;
  }

  function refresh(){
    var q=search ? String(search.value||'').toLowerCase() : '';
    var a=age ? age.value : 'all';
    var m=mode ? mode.value : 'all';
    var r=region ? region.value : 'default';
    var shown=0;
    for(var i=0;i<cards.length;i++){
      var c=cards[i];
      var ca=c.getAttribute('data-age')||'u13';
      var cm=' '+(c.getAttribute('data-mode')||'')+' ';
      var cp=' '+(c.getAttribute('data-policy')||'default')+' ';
      var text=(c.textContent||c.innerText||'').toLowerCase();
      var okAge=(a==='all') || ageRank(ca)<=ageRank(a);
      var okMode=(m==='all') || cm.indexOf(' '+m+' ')!==-1;
      var okRegion=cp.indexOf(' '+r+' ')!==-1;
      var okSearch=!q || text.indexOf(q)!==-1;
      var ok=okAge && okMode && okRegion && okSearch;
      if(ok){c.className=c.className.replace(/\s*hidden/g,'');shown++;}
      else if(c.className.indexOf('hidden')===-1){c.className+=' hidden';}
    }
    if(msg){msg.innerHTML=shown+' title'+(shown===1?'':'s')+' shown.';}
  }

  if(age) age.onchange=refresh;
  if(mode) mode.onchange=refresh;
  if(region) region.onchange=refresh;
  if(search) search.onkeyup=refresh;
  refresh();
}());
