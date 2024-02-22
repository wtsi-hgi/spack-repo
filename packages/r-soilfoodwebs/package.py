# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilfoodwebs(RPackage):
	"""Soil Food Web Analysis

	Analyzing soil food webs or any food web measured at equilibrium. The package
  calculates carbon and nitrogen fluxes and stability properties using methods
  described by Hunt et al. (1987) <doi:10.1007/BF00260580>, de Ruiter et al. 
  (1995) <doi:10.1126/science.269.5228.1257>, Holtkamp et al. (2011)
  <doi:10.1016/j.soilbio.2010.10.004>, and Buchkowski and Lindo (2021) 
  <doi:10.1111/1365-2435.13706>. The package can also manipulate the structure 
  of the food web as well as simulate food webs away from equilibrium and run 
  decomposition experiments.
	"""
	
	cran = "soilfoodwebs" 

	version("1.0.2", md5="cf05bde6648624ffcc20f5955a0e7481")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-diagram@1.6.5:", type=("build", "run"))
	depends_on("r-quadprog@1.5.8:", type=("build", "run"))
	depends_on("r-lpsolve@5.6.15:", type=("build", "run"))
	depends_on("r-rootsolve@1.8.2.2:", type=("build", "run"))
	depends_on("r-desolve@1.28:", type=("build", "run"))
