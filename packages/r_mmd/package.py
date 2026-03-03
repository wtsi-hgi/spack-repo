# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmd(RPackage):
	"""Minimal Multilocus Distance (MMD) for Source Attribution and
Loci Selection

	The aim of the package is two-fold: (i) To implement 
    the MMD method for attribution of individuals to sources using 
    the Hamming distance between multilocus genotypes. (ii) To select 
    informative genetic markers based on information theory concepts 
    (entropy, mutual information and redundancy). The package implements the 
    functions introduced by Perez-Reche, F. J., Rotariu, O., Lopes, B. S., 
    Forbes, K. J. and Strachan, N. J. C. Mining whole genome sequence data to 
    efficiently attribute individuals to source populations. 
    Scientific Reports 10, 12124 (2020) <doi:10.1038/s41598-020-68740-6>.
    See more details and examples in the README file.
	"""
	
	cran = "MMD" 

	version("1.0.0", md5="e3177fcfa8dfcaed0283a2128b763735")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
