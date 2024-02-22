# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegan3d(RPackage):
	"""Static and Dynamic 3D Plots for the 'vegan' Package

	Static and dynamic 3D plots to be used with ordination
    results and in diversity analysis, especially with the vegan package.
	"""
	
	homepage = "https://cran.r-project.org/"
	cran = "vegan3d" 

	version("1.2-0", md5="31fa0613a6fd2c189eb70ec3f8ffbfc2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-vegan@2.3.0:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-scatterplot3d@0.3.40:", type=("build", "run"))
