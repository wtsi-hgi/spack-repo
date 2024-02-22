# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBingat(RPackage):
	"""Binary Graph Analysis Tools

	Tools to analyze binary graph objects.
	"""
	
	cran = "bingat" 

	version("1.3", md5="36880c9471862d7a9b96c0d934a1d50b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
