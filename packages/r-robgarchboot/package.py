# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobgarchboot(RPackage):
	"""Robust Bootstrap Forecast Densities for GARCH Models

	Bootstrap forecast densities for GARCH (Generalized Autoregressive Conditional Heteroskedastic) returns and volatilities using the robust residual-based bootstrap procedure of Trucios, Hotta and Ruiz (2017) <DOI:10.1080/00949655.2017.1359601>.
	"""
	
	cran = "RobGARCHBoot" 

	version("1.2.0", md5="9c8845d630966f486c9c5f048093ff7e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
