(function(){var tm=document.querySelector('[data-tm]');if(!tm)return;var ss=[].slice.call(tm.querySelectorAll('.tm-s')),line=tm.querySelector('.tm-line'),T=[];
var W=[0.04,0.4,0.74,1],rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
function set(k,fin){ss.forEach(function(s,i){s.classList.toggle('on',i<=k);s.classList.toggle('cur',i===k&&!fin)});
 var m=matchMedia('(max-width:900px)').matches;line.style.setProperty('--p',fin?1:(m?[0.04,0.5,0.9][k]:W[k]));line.style.setProperty('--end',fin?1:0)}
function clear(){T.forEach(clearTimeout);T=[]}
function play(){clear();tm.classList.add('tm-js');ss.forEach(function(s){s.classList.remove('on','cur')});line.style.setProperty('--p',0);line.style.setProperty('--end',0);
 if(rm){set(2,true);return}
 [0,1,2].forEach(function(k){T.push(setTimeout(function(){set(k)},500+k*1400))});T.push(setTimeout(function(){set(2,true)},500+2*1400+900))}
ss.forEach(function(s,i){s.querySelector('.tm-n').addEventListener('click',function(){clear();tm.classList.add('tm-js');set(i,i===2&&false)})});
tm.querySelector('.tm-re').addEventListener('click',play);
tm.classList.add('tm-js');ss.forEach(function(s){s.classList.add('on')});line.style.setProperty('--p',1);line.style.setProperty('--end',1);
if('IntersectionObserver' in window){var o=new IntersectionObserver(function(en){if(en[0].isIntersecting){o.disconnect();play()}},{threshold:.45});o.observe(tm)}
})();
