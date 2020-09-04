/**************************************************************************
* Changes to this file test them on authoring site first (publish Web only)
* Once tested on authoring site Publish to Live
* And request PO for CDN purge
***************************************************************************/

$(window).on("load", function () {
  /****** This is for FXCM Links *****/
  $(".section-wrapper.alert-section .alert__message .alert__link.FXCM").on("tap click", function (e) {
		var cookieName = "FXCM_CUSTOMER";

		var expires = 365;
		cookies().set(cookieName, "CLICKED", expires, "/");
		return true;
  });
  /****** End FXCM Links *****/
  
  /****** This is for Charts Iframe *****/
  /*FOREX sites*/
  if($("#EmbedChartsScript").length) {
	try {
		var _iframeElement = $('#EmbedChartsScript');
		var _hideTop = _iframeElement.data("hide-top-panel");
		_hideTop = _hideTop==undefined? true : _hideTop;
		var _hideLeft = _iframeElement.data("hide-left-panel");
		_hideLeft = _hideLeft==undefined? true : _hideLeft;
		var _product = $('#EmbedChartsScript').attr('name');
		if(_product == "myiFrame"){
			var url = window.location.href.split("?")[0].split("#")[0];
			var tokenArray = url.split('/');
			var lastToken = tokenArray[tokenArray.length - 1];
			_product = lastToken.split('?')[0];
		}
		url = "https://tradertoolkit.efxnow.com/DemoAdvancedCharts/?market=" + _product.toUpperCase().replace("_", "/") + "&period=15&HideToptoolbar=" + _hideTop + "&HideLeftSideToolbar=" + _hideLeft;
		$('#EmbedChartsScript').attr('src', url);
	}
	catch(err) {
		;
	}
  };
  /*City sites*/
  if($("#EmbedChartsScriptCity").length) {
	try {
		var _iframeElement = $('#EmbedChartsScriptCity');
		var _hideTop = _iframeElement.data("hide-top-panel");
		_hideTop = _hideTop==undefined? true : _hideTop;
		var _hideLeft = _iframeElement.data("hide-left-panel");
		_hideLeft = _hideLeft==undefined? true : _hideLeft;
		var _product = $('#EmbedChartsScriptCity').attr('name');
		if(_product == "myiFrame"){
			var url = window.location.href.split("?")[0].split("#")[0];
			var tokenArray = url.split('/');
			var lastToken = tokenArray[tokenArray.length - 1];
			_product = lastToken.split('?')[0];
		}
		url = "https://trade.loginandtrade.com/chartslite/?TA=dm003382&SN=376c5e56-bc03-49fb-9c3a-c6635d0ff41f&CUID=69&UN=dm003382&LO=default&IV=MINUTE&SP=5&PB=5000&BD=CIL&TH=light&MK=99500&SM=true#/";
		$('#EmbedChartsScriptCity').attr('src', url);
	}
	catch(err) {
		;
	}
  };
  /****** END Charts Iframe *****/

    /****** This is for back to top button *****/
	// How far the user will scroll before showing button
  	var scrollTravel = 640;
	// Add back to top button to page
  	$("body").append("<div class='btn-top'>&#9650;</div>");

	$(document).scroll(function() {
		if ($(document).scrollTop() >= scrollTravel) {
			$(".btn-top").css('display','block');
	  	} else {
			$(".btn-top").css('display','none');
		}
	});

	$(".btn-top").click(function() {
		$("html, body").animate({ scrollTop: 0 }, "slow");
		return false;
	})
  /****** END Back to top button *****/
});