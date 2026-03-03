# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenfa(RPackage):
	"""Single- And Multiple-Group Penalized Factor Analysis

	Fits single- and multiple-group penalized factor analysis models 
    via a trust-region algorithm with integrated automatic multiple tuning 
    parameter selection (Geminiani et al., 2021 <doi:10.1007/s11336-021-09751-8>). 
    Available penalties include lasso, adaptive lasso, scad, mcp, and ridge. 
	"""
	
	homepage = "https://github.com/egeminiani/penfa"
	cran = "penfa" 

	version("0.1.1", md5="1de0baf60ee16c7cff55285100607146")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-gjrm", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
