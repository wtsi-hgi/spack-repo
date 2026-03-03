# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSphunif(RPackage):
	"""Uniformity Tests on the Circle, Sphere, and Hypersphere

	Implementation of uniformity tests on the circle and
    (hyper)sphere. The main function of the package is unif_test(), which
    conveniently collects more than 30 tests for assessing uniformity on
    S^{p-1}={x in R^p : ||x||=1}, p >= 2. The test statistics are implemented
    in the unif_stat() function, which allows computing several statistics to
    several samples within a single call, thus facilitating Monte Carlo
    experiments. Furthermore, the unif_stat_MC() function allows
    parallelizing them in a simple way. The asymptotic null distributions of
    the statistics are available through the function unif_stat_distr(). The
    core of 'sphunif' is coded in C++ by relying on the 'Rcpp' package.
    The package also provides several novel datasets and gives the
    replicability for the data application in García-Portugués,
    Navarro-Esteban and Cuesta-Albertos (2023) <arXiv:2008.09897>.
	"""
	
	homepage = "https://github.com/egarpor/sphunif"
	cran = "sphunif" 

	version("1.3.0", md5="d834ff19c7307026aeeec6fbd482e687")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-rotasym", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
