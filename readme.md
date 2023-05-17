## Pygebraic -Still a WIP-

Pygebraic is supposed to be a nice tool to solve algebraic expressions: You provide a string representing of an algebraic expresion and possibly an operation to be performed on it and `pygebraic` will solve it for you along with the steps towards the solution and (why not) also possibly a file that you can print (pdf or some other human-friendly format) where you can see the input, the solution and the steps that led to that solution.

## How to Use it:

- Clone this repo
- cd into the repo's folder
- run `docker build -t <whatever_tag_you_like_> .`
- run `./run tests` (this will create a container, run the unit tests and exit
- Alternatively you could spawn an `ipython` shell typing `./run ipython`
- You can see the list of commands that you can run is you inspect `run` script.

That's it for now, as time allows me i'll keep enhancing the tool, for now the major goal is to:

- Compute Sum, Substraction, Multiplication and Division of Monomies and Polinomies.

The end goal is to have a tool that can:

- Perform all the operations on an Algebraic expression like:
  - Factorization.
  - MCD
  - MCM
  - Fraction Operation & simplification
  - Equations
  - System of Equations
  - and more...
