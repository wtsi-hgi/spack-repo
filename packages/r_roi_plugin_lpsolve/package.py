# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginLpsolve(RPackage):
	"""'lp_solve' Plugin for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
             with the 'lp_solve' solver.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.lpsolve" 

	version("1.0-2", md5="930ca8dca637198e9fedf487ad570368")

	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2.0.1:", type=("build", "run"))
