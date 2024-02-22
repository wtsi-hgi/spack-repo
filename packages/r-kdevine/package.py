# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdevine(RPackage):
	"""Multivariate Kernel Density Estimation with Vine Copulas

	Implements the vine copula based kernel density estimator of
    Nagler and Czado (2016) <doi:10.1016/j.jmva.2016.07.003>. The estimator does
    not suffer from the curse of dimensionality and is therefore well suited for
    high-dimensional applications.
	"""
	
	homepage = "https://github.com/tnagler/kdevine"
	cran = "kdevine" 

	version("0.4.4", md5="d9233a57165e4c749508bb9c9bd33ff8")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-cctools", type=("build", "run"))
	depends_on("r-kdecopula@0.8.1:", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
