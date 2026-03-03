# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurfacetortoise(RPackage):
	"""Find Optimal Sampling Locations Based on Spatial Covariate(s)

	Create sampling designs using the surface reconstruction algorithm.
  Original method by: Olsson, D. 2002. A method to optimize soil sampling from 
  ancillary data. Poster presenterad at: NJF seminar no. 336, 
  Implementation of Precision Farming in Practical Agriculture, 10-12 
  June 2002, Skara, Sweden.
	"""
	
	homepage = "https://CRAN.R-project.org/package=SurfaceTortoise"
	cran = "SurfaceTortoise" 

	version("2.0.1", md5="ca030a0f161f86391e172bc35fa24e5f")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
