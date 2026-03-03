# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrr(RPackage):
	"""Reduced-Rank Regression

	Reduced-rank regression, diagnostics and graphics.
	"""
	
	homepage = "http://github.com/chrisaddy/rrr"
	cran = "rrr" 

	version("1.0.0", md5="7d918c65a7ff969b34f58aeead8505ac")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
