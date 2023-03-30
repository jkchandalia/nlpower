fine tuning methods and trade-offs
- freeze bert base and train final classification layer
- retrain the whole thing using the current weights as a starting place
- architecture diagram of bert based model + classification layer
- optimizers
- learning rates
- epochs and early stopping (based on a performance metric)
- modify code to add early stopping and use a validation set for early stopping

- have more bare bones pytorch implementation available for them to play with / look at on their own


extra stuff to potentially cover:
- how to use google colab
- hugging face datasets
- trainer library


Deadline for recorded part 2: night of April 4th (look at april 5th 6hr training)
video chat friday the 7th

part 3 narrowly scoped for april 4th deadline:
- goal : new member of the community
    - creating a hugging face account
    - overview of hugging face functionality (datasets)
        - creating your own dataset (from csv -> hugging face dataset)
        - uploading model to hugging face repo
