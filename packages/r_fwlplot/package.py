# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwlplot(RPackage):
	"""Scatter Plot After Residualizing Using 'fixest' Package

	Creates a scatter plot after residualizing using a set of covariates. The residuals are calculated using the 'fixest' package which allows very fast estimation that scales. Details of the (Yule-)Frisch-Waugh-Lovell theorem is given in Basu (2023) <arXiv:2307.00369>.
	"""
	
	cran = "fwlplot" 

	version("0.2.0", md5="644312fb199b7d1664373663fe64214f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
