# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvtsplot(RPackage):
	"""Multivariate Time Series Plot

	A function for plotting multivariate time series data.
	"""
	
	homepage = "https://github.com/rdpeng/mvtsplot"
	cran = "mvtsplot" 

	version("1.0-4", md5="b8e6734d9d23b0c34f77d86fe5a11c4d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
