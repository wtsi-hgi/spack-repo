# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasanoFranceschiniTest(RPackage):
	"""Fasano-Franceschini Test: A Multivariate Kolmogorov-Smirnov
Two-Sample Test

	An implementation of the two-sample multivariate
    Kolmogorov-Smirnov test described by Fasano and Franceschini (1987)
    <doi:10.1093/mnras/225.1.155>. This test evaluates the null hypothesis
    that two i.i.d. random samples were drawn from the same underlying
    probability distribution. The data can be of any dimension, and can be
    of any type (continuous, discrete, or mixed).
	"""
	
	homepage = "https://github.com/braunlab-nu/fasano.franceschini.test"
	cran = "fasano.franceschini.test" 

	version("2.2.2", md5="2de555fb5521eeddc114722e500e8782")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
