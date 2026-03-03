# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeatmap3(RPackage):
	"""An Improved Heatmap Package

	An improved heatmap package. Completely
    compatible with the original R function 'heatmap',
    and provides more powerful and convenient features.
	"""
	
	cran = "heatmap3" 

	version("1.1.9", md5="0bf9e7c9efab40a20f20871c91867bf4", url="https://cran.r-project.org/src/contrib/heatmap3_1.1.9.tar.gz")

	depends_on("r-fastcluster", type=("build", "run"))
