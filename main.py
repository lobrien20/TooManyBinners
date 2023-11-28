#!/usr/bin/env python3
import argparse
from src import binning
# Needs to take the following arguments:
# threads,contigs,reads,individual_binners,minimum_contig_length
# 
def main():
    
    parser = argparse.ArgumentParser(description="TooManyBinners help")
    
    parser.add_argument("-t", "--threads", help="Threads", required=True)
    parser.add_argument("-fw", "--forward-reads", help="Forward read path", required=True)
    parser.add_argument("-rev", "--reverse-reads", help="reverse read path", required=True)
    parser.add_argument("-contigs", "--contig-path", help="contig file path, if not provided will auto assemble")
    parser.add_argument("--minimum-contig-length", help="minium size of contigs for binning. Default is 2000.", default=2000)
    parser.add_argument("-b", "--individual-binners", help="Pick individual binners with commas, choices are: Semibin2,Maxbin2,Metabat2,Vamb,CONCOCT", required=True)
    parser.add_argument("-o", "--output-directory", help="Output directory_path", required=True)
    parser.add_argument("-c", "--custom-kmer-lengths", help="Custom kmer lengths for metaspades assembly (will default to auto)")
    parser.add_argument("-us", "--using-scaffolds", help="Using metaspades assembly scaffolds?")
    parser.add_argument("-m", "--memory", help="Available memory (in GB)", default='100', type=str)
    parser.add_argument    
    subparser = parser.add_subparsers()
    
    parser.add_argument("--enable-betterbins-ensemble", help='Run betterbins ensemble binning?', action='store_true')


    parser.add_argument("--checkm2-db-path", help="Database for checkm2 prokaryotic refining")
    parser.add_argument("--eukaryotic_database_path", help="eukaryotic database (any BUSCO database can technically be used) for Compleasm eukaryotic refining")
    if args.enable_betterbins_ensemble:
        if not args.checkm2_db_path or not args.eukaryotic_database_path:
            parser.error("--checkm2-db-path and --eukaryotic_database_path arguments are required when enable-betterbins-ensemble was set.")




    args = parser.parse_args()
    sample_name = "_sample_result"
    forward_read_file_name = args.forward_reads.split("/")[-1]
    reverse_read_file_name = args.reverse_reads.split("/")[-1]
    for fwd,rev in zip(forward_read_file_name, reverse_read_file_name):
        if fwd == rev:
            sample_name = sample_name + fwd
        else:
            break
    contig_abundances,the_binner = binning.setup_binning(args, sample_name)
    binner = binning.run_binning(args.output_directory, the_binner, ",".join(args.individual_binners))
    binner.run_final_ensemble_binning(args.checkm2_db_path, args.eukaryotic_database_path)


main()
