/* Cooltivo · entrada ao rolar: mesma animação em todas as páginas */
(function(){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches||!('IntersectionObserver' in window))return;
  var D=document,STEP=90,MAX=4;
  var SKIP='.capa,.clients,.player,.wa-fab,nav,footer,[data-nomotion],.tese-frases,.toc,[data-toc]';
  var LAYOUT=/(^|\s)(grid|head|ch-grid|cols|inner)(\s|$)/;
  function kids(el){return Array.prototype.filter.call(el.children,function(c){return !/^(SCRIPT|STYLE|SVG|BUTTON)$/i.test(c.tagName)&&!c.matches('svg,.bg-sym,.arr,[aria-hidden="true"]')})}
  function expand(el,out){
    var k=kids(el);
    if(LAYOUT.test(el.className)||el.classList.contains('wrap')){k.forEach(function(c){add(c,out)});return}
    out.push(el)
  }
  function add(c,out){
    if(c.matches(SKIP)||c.closest(SKIP))return;
    if(LAYOUT.test(c.className)&&kids(c).length){kids(c).forEach(function(x){add(x,out)});return}
    var k=kids(c);
    // listas de cartões (3 ou mais blocos irmãos): cada um entra no seu tempo
    if(k.length>=3&&k.every(function(x){return x.tagName===k[0].tagName&&/^(ARTICLE|LI|DIV|A)$/.test(x.tagName)})&&c.getBoundingClientRect().height>0&&!c.matches('.pills,.chips,.chips2,.marquee,.track,.slides,.c3,.row,.facts,.nums,.ctas')){k.forEach(function(x){add(x,out)});return}
    out.push(c)
  }
  function collect(){
    var out=[];
    D.querySelectorAll('header.ch .ch-txt').forEach(function(t){kids(t).forEach(function(x){out.push(x)})});
    D.querySelectorAll('header.ch .ch-vid,header.ch .eco-vid').forEach(function(x){out.push(x)});
    D.querySelectorAll('section').forEach(function(s){
      if(s.matches(SKIP))return;
      var w=s.querySelector(':scope > .wrap')||s;
      kids(w).forEach(function(c){add(c,out)})
    });
    return out.filter(function(e,i){return out.indexOf(e)===i&&!out.some(function(o){return o!==e&&o.contains(e)})})
  }
  function run(){
    var items=collect(),io=new IntersectionObserver(function(es){
      var vis=es.filter(function(e){return e.isIntersecting}).sort(function(a,b){return items.indexOf(a.target)-items.indexOf(b.target)});
      vis.forEach(function(e,i){
        var t=e.target;io.unobserve(t);
        t.style.setProperty('--rvd',(Math.min(i,MAX)*STEP/1000)+'s');
        requestAnimationFrame(function(){requestAnimationFrame(function(){t.classList.add('in')})});
        var done=function(ev){if(ev&&ev.target!==t)return;t.removeEventListener('transitionend',done);t.classList.remove('rv','in');t.style.removeProperty('--rvd')};
        t.addEventListener('transitionend',done);
        setTimeout(done,2200)
      })
    },{threshold:.08,rootMargin:'0px 0px -6% 0px'});
    items.forEach(function(e){e.classList.add('rv');io.observe(e)})
  }
  if(D.readyState==='loading')D.addEventListener('DOMContentLoaded',run);else run()
})();
