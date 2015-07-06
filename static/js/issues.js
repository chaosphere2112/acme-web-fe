function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires=" + date.toGMTString();
    }
    else var expires = "";

    var fixedName = '<%= Request["formName"] %>';
    name = fixedName + name;

    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}

function ajax_json(url, method, success, data, failure) {
	var csrf = readCookie("csrftoken");
	
	headers = { "X-CSRFToken": csrf };
	settings = {"accepts":"application/json", "contentType":"application/json"};

	function json_succeed(d, status, jqXHR) {
		var j = JSON.parse(d);
		if (success !== undefined) {
			success(j);
		}
	}

	settings["success"] = json_succeed;
	settings["method"] = method;
	settings["headers"] = headers

	if (data !== undefined) {
		if (method !== "GET") {
			settings["data"] = JSON.stringify(data);
		} else {
			settings["data"] = data;
		}
	}
	if (failure !== undefined) {
		settings["error"] = failure
	}
	return $.ajax(url, settings);
}