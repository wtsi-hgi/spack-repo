# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtrcool(RPackage):
	"""Feature Extraction from Biological Sequences

	Extracts features from biological sequences. It contains most features which are presented in related work and also includes features which have never been introduced before. It extracts numerous features from nucleotide and peptide sequences. Each feature converts the input sequences to discrete numbers in order to use them as predictors in machine learning models. There are many features and information which are hidden inside a sequence. Utilizing the package, users can convert biological sequences to discrete models based on chosen properties. References: 'iLearn' 'Z. Chen et al.' (2019) <DOI:10.1093/bib/bbz041>. 'iFeature' 'Z. Chen et al.' (2018) <DOI:10.1093/bioinformatics/bty140>. <https://CRAN.R-project.org/package=rDNAse>. 'PseKRAAC' 'Y. Zuo et al.' 'PseKRAAC: a flexible web server for generating pseudo K-tuple reduced amino acids composition' (2017) <DOI:10.1093/bioinformatics/btw564>. 'iDNA6mA-PseKNC' 'P. Feng et al.' 'iDNA6mA-PseKNC: Identifying DNA N6-methyladenosine sites by incorporating nucleotide physicochemical properties into PseKNC' (2019) <DOI:10.1016/j.ygeno.2018.01.005>. 'I. Dubchak et al.' 'Prediction of protein folding class using global description of amino acid sequence' (1995) <DOI:10.1073/pnas.92.19.8700>. 'W. Chen et al.' 'Identification and analysis of the N6-methyladenosine in the Saccharomyces cerevisiae transcriptome' (2015) <DOI:10.1038/srep13859>. 
	"""
	
	cran = "ftrCOOL" 

	version("2.0.0", md5="0d0beab1a156fcfee545f0e6faa031e3")

