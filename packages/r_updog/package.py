# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdog(RPackage):
	"""Flexible Genotyping for Polyploids

	Implements empirical Bayes approaches to genotype
       polyploids from next generation sequencing data while
       accounting for allele bias, overdispersion, and sequencing
       error. The main functions are flexdog() and multidog(), 
       which allow the specification
       of many different genotype distributions. Also provided are functions to
       simulate genotypes, rgeno(), and read-counts, rflexdog(), as well as
       functions to calculate oracle genotyping error rates, oracle_mis(), and
       correlation with the true genotypes, oracle_cor(). These latter two
       functions are useful for read depth calculations. Run
       browseVignettes(package = "updog") in R for example usage. See
       Gerard et al. (2018) <doi:10.1534/genetics.118.301468> and
       Gerard and Ferrao (2020) <doi:10.1093/bioinformatics/btz852> for details 
       on the implemented methods.
	"""
	
	homepage = "https://github.com/dcgerard/updog/"
	cran = "updog" 

	version("2.1.5", md5="3a29a30707474c783054bdcd5e20346a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
