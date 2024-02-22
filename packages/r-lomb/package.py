# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLomb(RPackage):
	"""Lomb-Scargle Periodogram

	Computes the Lomb-Scargle Periodogram for unevenly sampled time series. Includes a randomization procedure to obtain exact p-values.
	"""
	
	cran = "lomb" 

	version("2.2.0", md5="bdb906cbcaaa7d2f1307818f5365dec7")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
