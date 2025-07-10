# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwasBayes(RPackage):
	"""Bayesian analysis of Gaussian GWAS data

	This package is built to perform GWAS analysis using Bayesian techniques. Currently, GWAS.BAYES has functionality for the implementation of BICOSS for Gaussian phenotypes (Williams, J., Ferreira, M. A., and Ji, T. (2022). BICOSS: Bayesian iterative conditional stochastic search for GWAS. BMC Bioinformatics 23, 475). The research related to this package was supported in part by National Science Foundation awards DMS 1853549, DMS 1853556, and DMS 2054173.
	"""
	
	bioc = "GWAS.BAYES" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GWAS.BAYES_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GWAS.BAYES/GWAS.BAYES_1.12.0.tar.gz"]

	version("1.12.0", sha256="4b7b8bd9f541a6dba8ac812683bc160def6b8605d1fca7a86ff5887b2cb97fec")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ga@3.2:", type=("build", "run"))
	depends_on("r-caret@6.0.86:", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-limma@3.54:", type=("build", "run"))
	depends_on("r-mass@7.3.58.1:", type=("build", "run"))
