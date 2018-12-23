var data = [
{problem:"http://hope.simons-rock.edu/~mbarsky/intro19/tutorials/functions/func_number_of_cents.py", 
solution:"http://hope.simons-rock.edu/~mbarsky/intro19/tutorials/functions/func_number_of_cents_solution.py",
hint:"hint0.html",
explanation:"http://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/NumberOfcentsExplanation.mp4"}];

var current_problem = -1;
var current_included = 1;

var problems = new Array(data.length);


for (var i=0; i<problems.length; i++){
	problems[i] = 1;
}

function load_problem(id){
	current_problem = id;
	current_included = problems[current_problem];
	var iframe_elem = document.getElementById("contentframe");
	iframe_elem.src = data[current_problem].problem;
	show_buttons();
}


function show_buttons(){
	var buttons_elem = document.getElementById("buttons");
	if (current_problem >=0){
		buttons_elem.style.display = "inline-block";
	}
	else {
		buttons_elem.style.display = "none";
	}
}

function show_task(){
	var iframe_elem = document.getElementById("contentframe");
	iframe_elem.src = data[current_problem].problem;
	show_buttons();
}

function show_hint(){
	var iframe_elem = document.getElementById("contentframe");
	iframe_elem.src = data[current_problem].hint;
	show_buttons();
}

function show_solution(){
	var iframe_elem = document.getElementById("contentframe");
	iframe_elem.src = data[current_problem].solution;
	show_buttons();
}

function show_explanation(){
	var iframe_elem = document.getElementById("contentframe");
	iframe_elem.src = data[current_problem].explanation;
	show_buttons();
}

function mark_completed(){
	var include_elem = document.getElementById("completed");
	if (current_included == 1){
		include_elem.innerHTML = "Show again";
		current_included = 0;
		problems[current_problem] = 0;
	}
	else{
		include_elem.innerHTML = "Do not show again";
		current_included = 1;
		problems[current_problem] = 1;
	}
}