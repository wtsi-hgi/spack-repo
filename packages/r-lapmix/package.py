# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLapmix(RPackage):
	"""Laplace Mixture Model in Microarray Experiments

	Laplace mixture modelling of microarray experiments. A hierarchical Bayesian approach is used, and the hyperparameters are estimated using empirical Bayes. The main purpose is to identify differentially expressed genes.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "lapmix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/lapmix_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/lapmix/lapmix_1.68.0.tar.gz"]

	version("1.68.0", md5="5d2611d1b39b06b05ed64ffab459a5a9")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
