# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhctools(RPackage):
	"""Analysis of MHC Data in Non-Model Species

	Fifteen tools for bioinformatics processing and analysis of major 
    histocompatibility complex (MHC) data. The functions are tailored for amplicon data 
    sets that have been filtered using the dada2 method (for more information on 
    dada2, visit <https://benjjneb.github.io/dada2/> ), but even other types of data 
    sets can be analyzed.
    The ReplMatch() function matches replicates in data sets in order to evaluate 
    genotyping success.
    The GetReplTable() and GetReplStats() functions perform such an evaluation.
    The CreateFas() function creates a fasta file with all the sequences in the data 
    set.
    The CreateSamplesFas() function creates individual fasta files for each sample in 
    the data set.
    The DistCalc() function calculates Grantham, Sandberg, or p-distances from pairwise 
    comparisons of all sequences in a data set, and mean distances of all pairwise 
    comparisons within each sample in a data set. The function additionally outputs five 
    tables with physico-chemical z-descriptor values (based on Sandberg et al. 1998) for 
    each amino acid position in all sequences in the data set. These tables may be useful 
    for further downstream analyses, such as estimation of MHC supertypes.
    The BootKmeans() function is a wrapper for the kmeans() function of the 'stats'
    package, which allows for bootstrapping. Bootstrapping k-estimates may be
    desirable in data sets, where e.g. BIC- vs. k-values do not produce clear
    inflection points ("elbows"). BootKmeans() performs multiple runs of kmeans() and 
    estimates optimal k-values based on a user-defined threshold of BIC reduction. The 
    method is an automated and bootstrapped version of visually inspecting elbow plots 
    of BIC- vs. k-values.
    The ClusterMatch() function is a tool for evaluating whether different k-means() 
    clustering models identify similar clusters, and summarize bootstrap model stats as 
    means for different estimated values of k. It is designed to take files produced by 
    the BootKmeans() function as input, but other data can be analysed if the 
    descriptions of the required data formats are observed carefully.
    The PapaDiv() function compares parent pairs in the data set and calculate their 
    joint MHC diversity, taking into account sequence variants that occur in both 
    parents.
    The HpltFind() function infers putative haplotypes from families in the data 
    set. 
    The GetHpltTable() and GetHpltStats() functions evaluate the accuracy of 
    the haplotype inference.
    The CreateHpltOccTable() function creates a binary (logical) haplotype-sequence 
    occurrence matrix from the output of HpltFind(), for easy overview of which 
    sequences are present in which haplotypes. 
    The HpltMatch() function compares haplotypes to help identify overlapping and 
    potentially identical types.
    The NestTablesXL() function translates the output from HpltFind() to an Excel 
    workbook, that provides a convenient overview for evaluation and curating of the 
    inferred putative haplotypes.
	"""
	
	cran = "MHCtools" 

	version("1.5.3", md5="46775531b64f6240e32cec0e4677e93a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
