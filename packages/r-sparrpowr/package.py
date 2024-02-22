# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparrpowr(RPackage):
	"""Power Analysis to Detect Spatial Relative Risk Clusters

	Calculate the statistical power to detect clusters using kernel-based 
        spatial relative risk functions that are estimated using the 'sparr' package.
        Details about the 'sparr' package methods can be found in the tutorial: Davies
        et al. (2018) <doi:10.1002/sim.7577>. Details about kernel density estimation 
        can be found in J. F. Bithell (1990) <doi:10.1002/sim.4780090616>. More 
        information about relative risk functions using kernel density estimation can 
        be found in J. F. Bithell (1991) <doi:10.1002/sim.4780101112>.
	"""
	
	homepage = "https://github.com/machiela-lab/sparrpowR"
	cran = "sparrpowR" 

	version("0.2.8", md5="645194cb31f063e2aeb6eb22f699ebc9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
