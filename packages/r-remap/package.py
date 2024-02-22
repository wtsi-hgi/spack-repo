# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemap(RPackage):
	"""Regional Spatial Modeling with Continuous Borders

	Automatically creates separate regression models for different spatial 
    regions. The prediction surface is smoothed using a regional border smoothing 
    method. If regional models are continuous, the resulting prediction surface is 
    continuous across the spatial dimensions, even at region borders. Methodology 
    is described in Wagstaff and Bean (2023) <doi:10.32614/RJ-2023-004>.
	"""
	
	homepage = "https://github.com/jadonwagstaff/remap"
	cran = "remap" 

	version("0.3.1", md5="4f2014cdab01c83ca30d3f56ed373d01")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-units@0.6.7:", type=("build", "run"))
