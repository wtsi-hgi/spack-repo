# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeature(RPackage):
	"""Local Inferential Feature Significance for Multivariate Kernel
Density Estimation

	Local inferential feature significance for multivariate kernel density estimation.
	"""
	
	homepage = "https://www.mvstat.net/tduong/"
	cran = "feature" 

	version("1.2.15", md5="275b6203fb94af20a8e83514979d577c")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-ks@1.12:", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
