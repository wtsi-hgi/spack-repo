# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsaenet(RPackage):
	"""Multi-Step Adaptive Estimation Methods for Sparse Regressions

	Multi-step adaptive elastic-net (MSAENet) algorithm for
    feature selection in high-dimensional regressions proposed in
    Xiao and Xu (2015) <DOI:10.1080/00949655.2015.1016944>,
    with support for multi-step adaptive MCP-net (MSAMNet) and
    multi-step adaptive SCAD-net (MSASNet) methods.
	"""
	
	homepage = "https://nanx.me/msaenet/"
	cran = "msaenet" 

	version("3.1.1", md5="884c80221f22f646db20b1963d88af2f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg@3.8.0:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
