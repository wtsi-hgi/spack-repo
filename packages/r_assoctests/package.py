# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssoctests(RPackage):
	"""Genetic Association Studies

	Some procedures including EIGENSTRAT (a procedure for detecting and correcting 
	for population stratification through searching for the eigenvectors in genetic association 
	studies), PCoC (a procedure for correcting for population stratification through calculating 
	the principal coordinates and the clustering of the subjects), Tracy-Widom test (a procedure 
	for detecting the significant eigenvalues of a matrix), distance regression (a procedure for 
	detecting the association between a distance matrix and some independent variants of interest), 
	single-marker test (a procedure for identifying the association between the genotype at a 
	biallelic marker and a trait using the Wald test or the Fisher's exact test), MAX3 (a procedure 
	for testing for the association between a single nucleotide polymorphism and a binary phenotype 
	using the maximum value of the three test statistics derived for the recessive, additive, and 
	dominant models), nonparametric trend test (a procedure for testing for the association between 
	a genetic variant and a non-normal distributed quantitative trait based on the nonparametric 
	risk), and nonparametric MAX3 (a procedure for testing for the association between a biallelic 
	single nucleotide polymorphism and a quantitative trait using the maximum value of the three 
	nonparametric trend tests derived for the recessive, additive, and dominant models), which are 
	commonly used in genetic association studies. To cite this package in publications use: 
	Lin Wang, Wei Zhang, and Qizhai Li. AssocTests: An R Package for Genetic Association Studies. 
	Journal of Statistical Software. 2020; 94(5): 1-26.
	"""
	
	cran = "AssocTests" 

	version("1.0-1", md5="a6424925ac487ba7572faa57e1ca1f3b")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-fextremes", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
