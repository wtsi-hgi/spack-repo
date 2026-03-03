# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginScs(RPackage):
	"""'SCS' Plug-in for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
         with the 'SCS' solver for solving convex cone problems.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.scs" 

	version("1.1-2", md5="a7273e4eb2472a9567991cc6dedf0107")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-scs@3.2.4:", type=("build", "run"))
