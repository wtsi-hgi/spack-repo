# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCjamp(RPackage):
	"""Copula-Based Joint Analysis of Multiple Phenotypes

	We provide a computationally efficient and robust implementation of the recently proposed C-JAMP (Copula-based Joint Analysis of Multiple Phenotypes) method (Konigorski et al., 2019, submitted). C-JAMP allows estimating and testing the association of one or multiple predictors on multiple outcomes in a joint model, and is implemented here with a focus on large-scale genome-wide association studies with two phenotypes. The use of copula functions allows modeling a wide range of multivariate dependencies between the phenotypes, and previous results are supporting that C-JAMP can increase the power of association studies to identify associated genetic variants in comparison to existing methods (Konigorski, Yilmaz, Pischon, 2016, <DOI:10.1186/s12919-016-0045-6>; Konigorski, Yilmaz, Bull, 2014, <DOI:10.1186/1753-6561-8-S1-S72>). In addition to the C-JAMP functions, functions are available to generate genetic and phenotypic data, to compute the minor allele frequency (MAF) of genetic markers, and to estimate the phenotypic variance explained by genetic markers.
	"""
	
	cran = "CJAMP" 

	version("0.1.1", md5="bfc1d9c8d77bbb3c8f31fec67eb9bca7")

	depends_on("r-optimx", type=("build", "run"))
