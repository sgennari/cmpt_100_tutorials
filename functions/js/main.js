var data = [
{problem:"https://repl.it/@ArthurLi2017/Number-of-cents?lite=true", 
solution:"solutions/solution0.py",
hint:"hints/hint0.html",
explanation:"http://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/NumberOfcentsExplanation.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Total-slices?lite=true", 
solution:"solutions/solution1.py",
hint:"hints/hint1.html",
explanation:"self-exercises.html"},

{problem:"https://repl.it/@ArthurLi2017/Calculate-tax?lite=true", 
solution:"solutions/solution2.py",
hint:"hints/hint2.html",
explanation:"http://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/CalculateTaxExplanation.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Total-seconds?lite=true", 
solution:"solutions/solution3.py",
hint:"hints/hint3.html",
explanation:"self-exercises.html"},

{problem:"https://repl.it/@ArthurLi2017/Smaller-name?lite=true", 
solution:"solutions/solution4.py",
hint:"hints/hint4.html",
explanation:"https://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/RehearseExplanationReturnEarlierName.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Format-name?lite=true", 
solution:"solutions/solution5.py",
hint:"hints/hint5.html",
explanation:"https://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/RehearseExplanationFirstLast.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Phonebook-listing?lite=true", 
solution:"solutions/solution6.py",
hint:"hints/hint6.html",
explanation:"https://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/FunctionReuseExplanation.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Ticket-price?lite=true", 
solution:"solutions/solution7.py",
hint:"hints/hint7.html",
explanation:"https://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/RehearseExplanationDifferentPrices.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Calculate-grade?lite=true", 
solution:"solutions/solution8.py",
hint:"hints/hint8.html",
explanation:"self-exercises.html"},

{problem:"https://repl.it/@ArthurLi2017/Same-abs?lite=true", 
solution:"solutions/solution9.py",
hint:"hints/hint9.html",
explanation:"https://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/SameAbs.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Can-vote?lite=true", 
solution:"solutions/solution10.py",
hint:"hints/hint10.html",
explanation:"http://hope.simons-rock.edu/~mbarsky/intro18/tutorials/functions/CanVote.mp4"},

{problem:"https://repl.it/@ArthurLi2017/Same-ends?lite=true", 
solution:"solutions/solution11.py",
hint:"hints/hint11.html",
explanation:"self-exercises.html"}
];

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