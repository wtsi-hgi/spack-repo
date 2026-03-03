# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginQpoases(RPackage):
	"""'qpOASES' Plugin for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
         with the quadratic solver 'qpOASES'. More information about
         'qpOASES' can be found at <https://github.com/coin-or/qpOASES>.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.qpoases" 

	version("1.0-3", md5="2aaaf3369bb7c85f2b04707dc8d99f81")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
