# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginNloptr(RPackage):
	"""'nloptr' Plug-in for the 'R' Optimization Infrastructure

	Enhances the R Optimization Infrastructure ('ROI') package
        with the 'NLopt' solver for solving nonlinear optimization problems.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.nloptr" 

	version("1.0-1", md5="1b42fe855c324062d44eedf850c6287b")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-nloptr@1.2.1:", type=("build", "run"))
