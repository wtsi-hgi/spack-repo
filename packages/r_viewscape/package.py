# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViewscape(RPackage):
	"""Viewscape Analysis

	A collection of functions to make R a more effective viewscape analysis 
    tool for calculating viewscape metrics based on computing the viewable area for 
    given a point/multiple viewpoints and a digital elevation model.The method of calculating 
    viewscape metrics implemented in this package are based on the work of 
    Tabrizian et al. (2020) <doi:10.1016/j.landurbplan.2019.103704>. The algorithm of computing 
    viewshed is based on the work of 
    Franklin & Ray. (1994) <https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=555780f6f5d7e537eb1edb28862c86d1519af2be>.
	"""
	
	cran = "viewscape" 

	version("1.0.0", md5="a4ce39d54fd0138dc14ffbc8861e347e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-foresttools", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
