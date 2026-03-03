# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixmatrix(RPackage):
	"""Classification with Matrix Variate Normal and t Distributions

	Provides sampling and density functions for matrix
    variate normal, t, and inverted t distributions;  ML estimation for matrix
    variate normal and t distributions using the EM algorithm,
    including some restrictions on the parameters; and classification by linear and
    quadratic discriminant analysis for matrix variate normal and t
    distributions described in Thompson et al. (2019) <doi:10.1080/10618600.2019.1696208>.
    Performs clustering with matrix variate normal and t mixture models.
	"""
	
	homepage = "https://github.com/gzt/MixMatrix/"
	cran = "MixMatrix" 

	version("0.2.6", md5="3500dcf0cd8e500abf2522558e682513")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
