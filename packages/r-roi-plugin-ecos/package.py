# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginEcos(RPackage):
	"""'ECOS' Plugin for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
	     with the Embedded Conic Solver ('ECOS') for solving conic optimization problems.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.ecos" 

	version("1.0-2", md5="f15073bee9ec96cc988cad1b9e8f4bec")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-ecosolver@0.5.4:", type=("build", "run"))
