# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterpic(RPackage):
	"""Create a Spatial Raster from Plain Images

	Create a spatial raster, as the ones provided by 'terra',
    from regular pictures.
	"""
	
	homepage = "https://dieghernan.github.io/rasterpic/"
	cran = "rasterpic" 

	version("0.2.4", md5="bace1e7de9e3cd7d068c3e2521645477")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-png@0.1.5:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-terra@1.4.22:", type=("build", "run"))
