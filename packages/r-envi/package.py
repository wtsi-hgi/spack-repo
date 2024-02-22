# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvi(RPackage):
	"""Environmental Interpolation using Spatial Kernel Density
Estimation

	Estimates an ecological niche using occurrence data, covariates, and kernel
        density-based estimation methods. For a single species with presence and absence data,
        the 'envi' package uses the spatial relative risk function that is estimated using the
        'sparr' package. Details about the 'sparr' package methods can be found in the tutorial:
        Davies et al. (2018) <doi:10.1002/sim.7577>. Details about kernel density estimation can
        be found in J. F. Bithell (1990) <doi:10.1002/sim.4780090616>. More information about
        relative risk functions using kernel density estimation can be found in J. F. Bithell
        (1991) <doi:10.1002/sim.4780101112>.
	"""
	
	homepage = "https://github.com/lance-waller-lab/envi"
	cran = "envi" 

	version("0.1.19", md5="28a92caa1f4d0920fcacba28ded23c4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-cvauc", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
