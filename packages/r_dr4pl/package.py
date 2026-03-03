# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDr4pl(RPackage):
	"""Dose Response Data Analysis using the 4 Parameter Logistic (4pl)
Model

	Models the relationship between dose levels and responses in a pharmacological experiment using the 4 Parameter Logistic model. Traditional packages on dose-response modelling such as 'drc' and 'nplr' often draw errors due to convergence failure especially when data have outliers or non-logistic shapes. This package provides robust estimation methods that are less affected by outliers and other initialization methods that work well for data lacking logistic shapes. We provide the bounds on the parameters of the 4PL model that prevent parameter estimates from diverging or converging to zero and base their justification in a statistical principle. These methods are used as remedies to convergence failure problems.  Gadagkar, S. R. and Call, G. B. (2015) <doi:10.1016/j.vascn.2014.08.006> Ritz, C. and Baty, F. and Streibig, J. C. and Gerhard, D. (2015) <doi:10.1371/journal.pone.0146021>.
	"""
	
	homepage = "https://bitbucket.org/dittmerlab/dr4pl"
	cran = "dr4pl" 

	version("2.0.0", md5="f6ad4d96b5f41b182d6da7d72fa5a77d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
