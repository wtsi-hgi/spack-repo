# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialbss(RPackage):
	"""Blind Source Separation for Multivariate Spatial Data

	Blind source separation for multivariate spatial data based on simultaneous/joint diagonalization of (robust) local covariance matrices. This package is an implementation of the methods described in Bachoc, Genton, Nordhausen, Ruiz-Gazen and Virta (2020) <doi:10.1093/biomet/asz079>.
	"""
	
	cran = "SpatialBSS" 

	version("0.14-0", md5="7f37bee4dc429bcc85ed94d462c9ffdd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jade", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatialnp", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
