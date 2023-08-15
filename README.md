#TooManyBinners binning pipeline

Pipeline tool built in python used to generate metagenomic bins with a variety of different binning tools for MAG generation. The aim of the tool is to simplify the MAG generation process by minimising the configurations required and the individual steps needed. 

It can generate bin sets from either just one binning tool or all of them, which can be used for evaluating the best binning tool for the dataset, or used downstream for ensemble binning - this tool will also soon include an ensemble binner.

To be used as singularity image (singularity definition file included in the repo).

###Currently can generate bins from the following binners:
- Vamb
- SemiBin2
- CONCOCT
- MaxBin2
- Metabat2

Able to be used from contigs or reads (reads generated through Metaspades, alignment information for binning is generated through Bowtie2).

###Takes the following arguments:

"-t", "--threads", help="Threads", required=True
"-fw", "--forward-reads", help="Forward read path", required=True
"-rev", "--reverse-reads", help="reverse read path", required=True
"-contigs", "--contig-path", help="contig file path, if not provided will auto assemble"
"--minimum-contig-length", help="minium size of contigs for binning. Default is 2000."
"-b", "--individual-binners", help="Pick individual binners with commas, choices are: Semibin2,Maxbin2,Metabat2,Vamb,CONCOCT"
"-o", "--output-directory", help="Output directory_path", required=True
"-c", "--custom-kmer-lengths", help="Custom kmer lengths for metaspades assembly (will default to auto if not)".
"-us", "--using-scaffolds", help="Using metaspades assembly scaffolds?"

###Example:
```
singularity run --cleanenv files_from_local/TooManyBinners.sif -fw 2manyBinners_testing/test_data/cami_plant_samplereads_1_P1.fastq.gz \
-rev 2manyBinners_testing/test_data/cami_plant_samplereads_1_P2.fastq.gz \
-b Semibin2,Maxbin2,Metabat2,Vamb,CONCOCT \
-o 2manyBinners_testing/test_output/ -t 10 \
-us True
```

All binsfrom each bin set is produced are generated in a final bins directory.