# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoilr(RPackage):
	"""Models of Soil Organic Matter Decomposition

	Functions for modeling Soil Organic Matter decomposition
        in terrestrial ecosystems with linear and nonlinear systems of differential equations. 
        The package implements
        models according to the compartmental system representation described in 
        Sierra and others (2012) <doi:10.5194/gmd-5-1045-2012> and Sierra and others (2014)
        <doi:10.5194/gmd-7-1919-2014>.
	"""
	
	cran = "SoilR" 

	version("1.2.107", md5="8f1937548a820e6c463fca4359a16613")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
