# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStcos(RPackage):
	"""Space-Time Change of Support

	Spatio-temporal change of support (STCOS) methods are designed for statistical inference
	on geographic and time domains which differ from those on which the data were observed. In
	particular, a parsimonious class of STCOS models supporting Gaussian outcomes was introduced
	by Bradley, Wikle, and Holan <doi:10.1002/sta4.94>. The 'stcos' package contains tools which
	facilitate use of STCOS models.
	"""
	
	homepage = "https://github.com/holans/ST-COS"
	cran = "stcos" 

	version("0.3.1", md5="a9d67760639af647d4b847c3f11c843d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
