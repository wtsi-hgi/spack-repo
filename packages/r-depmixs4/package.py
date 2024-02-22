# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepmixs4(RPackage):
	"""Dependent Mixture Models - Hidden Markov Models of GLMs and
Other Distributions in S4

	Fits latent (hidden) Markov models on mixed categorical and continuous (time series) data, otherwise known as dependent mixture models, see Visser & Speekenbrink (2010, <DOI:10.18637/jss.v036.i07>).
	"""
	
	homepage = "https://depmix.github.io/"
	cran = "depmixS4" 

	version("1.5-0", md5="149707ddcdfb31ab2501990d32386b78", url="https://cran.r-project.org/src/contrib/depmixS4_1.5-0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
