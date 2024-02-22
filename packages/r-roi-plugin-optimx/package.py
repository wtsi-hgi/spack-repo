# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginOptimx(RPackage):
	"""'optimx' Plug-in for the 'R' Optimization Infrastructure

	Enhances the R Optimization Infrastructure ('ROI') package
        with the 'optimx' package.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.optimx" 

	version("1.0-1", md5="5f93adeb36f60434c9ba1f80fe69a40c")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
