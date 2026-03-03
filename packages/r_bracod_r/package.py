# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBracodR(RPackage):
	"""BRACoD: Bayesian Regression Analysis of Compositional Data

	The goal of this method is to identify associations between bacteria and an environmental variable in 16S or other compositional data. The environmental variable is any variable which is measure for each microbiome sample, for example, a butyrate measurement paired with every sample in the data. Microbiome data is compositional, meaning that the total abundance of each sample sums to 1, and this introduces severe statistical distortions. This method takes a Bayesian approach to correcting for these statistical distortions, in which the total abundance is treated as an unknown variable. This package runs the python implementation using reticulate.
	"""
	
	cran = "BRACoD.R" 

	version("0.0.2.0", md5="b0779bcfe448d52f1a3ed0dd7b585286")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
