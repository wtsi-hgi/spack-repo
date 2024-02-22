# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexteffect(RPackage):
	"""Discovering Latent Treatments in Text Corpora and Estimating
Their Causal Effects

	Implements the approach described in Fong and Grimmer (2016) <https://aclweb.org/anthology/P/P16/P16-1151.pdf> for 
	automatically discovering latent treatments from a corpus and estimating the average marginal component effect (AMCE) of 
	each treatment.  The data is divided into a training and test set.  The supervised Indian Buffet Process (sibp) is used 
	to discover latent treatments in the training set.  The fitted model is then applied to the test set to infer the values 
	of the latent treatments in the test set.  Finally, Y is regressed on the latent treatments in the test set to estimate 
	the causal effect of each treatment.
	"""
	
	cran = "texteffect" 

	version("0.3", md5="ad3cbdeb71d4107255f943baf85139bb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
