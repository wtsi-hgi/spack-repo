# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGater(RPackage):
	"""Flow/Mass Cytometry Gating via Spatial Kernel Density Estimation

	Estimates statistically significant marker combination values within
        which one immunologically distinctive group (i.e., disease case) is more associated than
        another group (i.e., healthy control), successively, using various combinations (i.e.,
        "gates") of markers to examine features of cells that may be different between
        groups. For a two-group comparison, the 'gateR' package uses the spatial relative risk
        function estimated using the 'sparr' package. Details about the 'sparr' package
        methods can be found in the tutorial: Davies et al. (2018) <doi:10.1002/sim.7577>. Details
        about kernel density estimation can be found in J. F. Bithell (1990) <doi:10.1002/sim.4780090616>.
        More information about relative risk functions using kernel density estimation can be
        found in J. F. Bithell (1991) <doi:10.1002/sim.4780101112>.
	"""
	
	homepage = "https://github.com/lance-waller-lab/gateR"
	cran = "gateR" 

	version("0.1.15", md5="36a3b55b442893b81883cb12d1033684")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-spatialpack", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
