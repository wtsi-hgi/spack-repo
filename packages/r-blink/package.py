# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlink(RPackage):
	"""Record Linkage for Empirically Motivated Priors

	An implementation of the model in Steorts (2015) <DOI:10.1214/15-BA965SI>, which performs Bayesian entity resolution for categorical and text data, for any distance function defined by the user. In addition, the precision and recall are in the package to allow one to compare to any other comparable method such as logistic regression, Bayesian additive regression trees (BART), or random forests. The experiments are reproducible and illustrated using a simple vignette. LICENSE: GPL-3 + file license. 
	"""
	
	cran = "blink" 

	version("1.1.0", md5="fd7446cf2847f76259524d805bda7078")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
