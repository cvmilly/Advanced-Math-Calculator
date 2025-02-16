function printLatex(){
	var input = document.getElementById("equation-input");
	var textarea = document.getElementById("id_textarea");
	var display = document.getElementById("equation-display");

	display.innerHTML = "$" + textarea.innerHTML + "$";
	MathJax.Hub.Queue(["Typeset", MathJax.Hub]);	
}

function insertSymbol(symbolID){
	//cursorCurrentParent
	//var input = document.getElementById("equation-input");
	var input = document.getElementById(cursorCurrentParent);
	var symbol = document.getElementById(symbolID);

	var newNode = document.createElement("div");

	if(symbolID == "frac"){
		var cursorLocation = document.getElementById("cursor").className;
		newNode.className = "fraction";
		newNode.id = "frac-" + cursorLocation;
		newNode.innerHTML = "<div id='num-" + cursorLocation + "' class='numerator empty'><div class='input-item'>&nbsp;</div></div><div id='den-" + cursorLocation + "'class='denominator empty'><div class='input-item'>&nbsp;</div></div>";
	}else{
		newNode.className = "input-item";
		newNode.innerHTML = symbol.innerHTML;
	}
	//newNode.appendChild(newContent);

	insertAtCursor(newNode, symbol.innerHTML);

	var textarea = document.getElementById("id_textarea");
	textarea.focus();
}


function insertAtCursor(newNode, character){
//cursorCurrentParent
	//var input = document.getElementById("equation-input");
	var input = document.getElementById(cursorCurrentParent);
	var cursor = document.getElementById("cursor");

	var inputItems = input.children;
	var found = false;
		for(var i = 1; i < inputItems.length-1; i++){
			if(inputItems[i].id == "cursor"){
				input.insertBefore(newNode, inputItems[i+1]);
				//necessary to update which element is the cursor element
				cursor = document.getElementById("cursor");
				cursor.className = i+1;
				//console.log("Before");
				moveCursor(i+1);
				//console.log("In here: " + textarea.innerHTML);
				//console.log("After");
//console.log("i+1 = " + inputItems[i+2].id);
				shiftContainers(i+1, 1);
				/*if(inputItems[i+2].className == "sup"){
					inputItems[i+2].id = "sup-" + (i + 1);
					console.log("HEAYH: " + inputItems[i+2].id);
				}*/

				found = true;
				i = inputItems.length;
				//console.log("i: " + i + " out of " + inputItems.length);
			}
		}
		if(!found){
			//console.log("Not found");
			input.appendChild(newNode);
			//console.log("Not found: " + inputItems.length);
			cursor = document.getElementById("cursor");
			cursor.className = inputItems.length-1;
			moveCursor(inputItems.length-1);
		}

		if(document.getElementById(cursorCurrentParent).parentElement.className == "fraction" && document.getElementById(cursorCurrentParent).children.length > 2){
			//console.log("INSERT IN NUM OR DENOM");
			document.getElementById(cursorCurrentParent).className = (document.getElementById(cursorCurrentParent).className.substring(0,9) == "numerator") ? "numerator" : "denominator";
		}

		interpretEquation();
}


function interpretEquation(){
	var input = document.getElementById("equation-input");
	var inputItems = input.children;

	var temp = "";

	for(var i = 0; i < inputItems.length; i++){
		if(inputItems[i].id == "cursor"){

		}else if(inputItems[i].className == "sup"){
			temp += "^{";
			smallerChildren = inputItems[i].children;
			for(var j = 0; j < smallerChildren.length; j++){
				if(smallerChildren[j].id != "cursor"){
					temp += smallerChildren[j].textContent;
				}
			}
			temp += "}";
		}else if(inputItems[i].className == "fraction"){
			temp += "(";
			numeratorChildren = inputItems[i].children[0].children;
			for(var j = 1; j < numeratorChildren.length; j++){
				if(numeratorChildren[j].id != "cursor"){
					temp += numeratorChildren[j].textContent;
				}
			}
			temp += ")/(";
			denominatorChildren = inputItems[i].children[1].children;
			for(var j = 1; j < denominatorChildren.length; j++){
				if(denominatorChildren[j].id != "cursor"){
					temp += denominatorChildren[j].textContent;
				}
			}
			temp += ")";
		}else{
			temp += inputItems[i].textContent;
		}
	}

	var textarea = document.getElementById("id_textarea");
	textarea.innerHTML = temp;

	//console.log(temp);
}