# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginQuadprog(RPackage):
	"""'quadprog' Plug-in for the 'R' Optimization Infrastructure

	Enhances the R Optimization Infrastructure ('ROI') package
    by registering the 'quadprog' solver. It allows for solving quadratic programming (QP)
    problems.
	"""
	
	homepage = "http://roi.r-forge.r-project.org/"
	cran = "ROI.plugin.quadprog" 

	version("1.0-1", md5="d3994d613f8ef0f8cfd08ba584289627")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
