# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDire(RPackage):
	"""Linear Regressions with a Latent Outcome Variable

	Fit latent variable linear models, estimating score distributions for groups of people, following Cohen and Jiang (1999) <doi:10.2307/2669917>. In this model, a latent distribution is conditional on students item response, item characteristics, and conditioning variables the user includes. This latent trait is then integrated out. This software is intended to fit the same models as the existing software 'AM' <https://am.air.org/>. As of version 2, also allows the user to draw plausible values.
	"""
	
	homepage = "https://american-institutes-for-research.github.io/Dire/"
	cran = "Dire" 

	version("2.2.0", md5="b6d7826aa596c66bffe84bf289f29dfd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
