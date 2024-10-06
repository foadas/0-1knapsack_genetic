<h2>Algorithm Overview</h2>

<p>The Genetic Algorithm used in this project follows these key steps:</p>

<ol>
  <li><strong>Initialization (Population Generation):</strong>
    <ul>
      <li>A population of chromosomes (potential solutions) is randomly generated.</li>
      <li>Each chromosome represents a subset of items, with 1 indicating that the item is selected and 0 indicating that it is not.</li>
    </ul>
  </li>

  <li><strong>Fitness Evaluation:</strong>
    <ul>
      <li>The fitness of each chromosome is calculated based on the total value of selected items, ensuring the weight and size constraints are satisfied.</li>
      <li>Chromosomes that exceed the constraints are given a fitness of zero.</li>
    </ul>
  </li>

  <li><strong>Selection:</strong>
    <ul>
      <li>Chromosomes are selected for reproduction based on their fitness values using a roulette wheel mechanism, favoring higher fitness values.</li>
    </ul>
  </li>

  <li><strong>Crossover:</strong>
    <ul>
      <li>Two chromosomes are selected as parents, and a crossover operation is performed at a random point to create a child solution.</li>
      <li>This process mimics the combination of genes from two parents in biology.</li>
    </ul>
  </li>

  <li><strong>Mutation:</strong>
    <ul>
      <li>After crossover, the child chromosome may undergo mutation with a certain probability. Mutation flips one or more bits in the chromosome to introduce variation in the population.</li>
    </ul>
  </li>

  <li><strong>Termination:</strong>
    <ul>
      <li>The algorithm continues for a predefined number of generations, refining the population through selection, crossover, and mutation.</li>
      <li>The best solution found during the generations is returned as the final result.</li>
    </ul>
  </li>
</ol>
