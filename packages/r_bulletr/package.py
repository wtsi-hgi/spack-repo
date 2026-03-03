# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBulletr(RPackage):
	"""Algorithms for Matching Bullet Lands

	Analyze bullet lands using nonparametric methods. We provide a
    reading routine for x3p files (see <http://www.openfmc.org> for more
    information) and a host of analysis functions designed to assess the
    probability that two bullets were fired from the same gun barrel.
	"""
	
	homepage = "https://github.com/erichare/bulletr"
	cran = "bulletr" 

	version("0.1", md5="0e68dff353d5df1c640b782e2b8c8933")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-smoother", type=("build", "run"))
