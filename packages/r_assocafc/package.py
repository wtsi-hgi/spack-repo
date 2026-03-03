# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssocafc(RPackage):
	"""Allele Frequency Comparison

	When doing association analysis one does not always have the 
   genotypes for the control population.  In such cases it may be 
   necessary to fall back on frequency based tests using well known sources 
   for the frequencies in the control population, for instance, from the 
   1000 Genomes Project.  The Allele Frequency Comparison ('AssocAFC') package 
   performs multiple rare variant association analyses in both population and 
   family-based GWAS (Genome-Wide Association Study) designs. It includes 
   three score tests that are based on the difference of the sum of allele 
   frequencies between cases and controls.  Two of these tests, Wcorrected() 
   and Wqls(), are collapsing-based tests and suffer from having protective 
   and risk variants. The third test, afcSKAT(), is a score test that 
   overcomes the mix of SNP (Single-Nucleotide Polymorphism) effect 
   directions. For more details see 
   Saad M and Wijsman EM (2017) <doi:10.1093/bib/bbx107>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "AssocAFC" 

	version("1.0.2", md5="dd9f99260d6fc9b83e36a96338e53f78")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
