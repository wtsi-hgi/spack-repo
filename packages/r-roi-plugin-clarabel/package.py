# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginClarabel(RPackage):
	"""'clarabel' Plug-in for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
         with the 'clarabel' solver for solving convex cone problems.
         More information about 'clarabel' can be found at
         <https://oxfordcontrol.github.io/ClarabelDocs/stable/>.
	"""
	
	homepage = "https://gitlab.com/roigrp/solver/roi.plugin.clarabel"
	cran = "ROI.plugin.clarabel" 

	version("0.3", md5="76195878b980b7079f1efedef01b45b9")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-clarabel@0.5.1:", type=("build", "run"))
