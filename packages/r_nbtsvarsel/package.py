# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbtsvarsel(RPackage):
	"""Variable Selection in a Specific Regression Time Series of
Counts

	Performs variable selection in sparse negative binomial GLARMA (Generalised Linear Autoregressive Moving Average) models. For further details we refer the reader to the paper Gomtsyan (2023), <arXiv:2307.00929>.
	"""
	
	cran = "NBtsVarSel" 

	version("1.0", md5="b2e72de5bc1d0edd7d17573819f5e0a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mpath", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
