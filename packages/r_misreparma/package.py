# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisreparma(RPackage):
	"""Misreported Time Series Analysis

	Provides a simple and trustworthy methodology for the analysis of misreported continuous time series. See Moriña, D, Fernández-Fontelo, A, Cabaña, A, Puig P. (2021) <arXiv:2003.09202v2>.
	"""
	
	cran = "MisRepARMA" 

	version("0.0.2", md5="82108c97120f865cd22d0458674d2e80")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
