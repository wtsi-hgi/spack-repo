# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdecopula(RPackage):
	"""Kernel Smoothing for Bivariate Copula Densities

	Provides fast implementations of kernel smoothing techniques for
    bivariate copula densities, in particular density estimation and resampling,
    see Nagler (2018) <doi:10.18637/jss.v084.i07>. 
	"""
	
	homepage = "https://github.com/tnagler/kdecopula"
	cran = "kdecopula" 

	version("0.9.2", md5="6547379085b7f27709a27ba8491de4a3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-qrng", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
