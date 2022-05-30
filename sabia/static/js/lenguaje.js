
jQuery(function($) {


    "use strict";
  
  
     /* ----------------------------------------------------------- */
     /*  Style Switcher
     /* ----------------------------------------------------------- */
  
      (function($) { "use strict";
         $(document).ready(function(){
             $('.style-switch-button').click(function(){
             $('.style-switch-wrapper').toggleClass('active');
             });
             $('a.close-styler').click(function(){
             $('.style-switch-wrapper').removeClass('active');
             });
        });
      })(jQuery);
    
});