# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginAlabama(RPackage):
	"""'alabama' Plug-in for the 'R' Optimization Infrastructure

	Enhances the R Optimization Infrastructure ('ROI') package
        with the 'alabama' solver for solving nonlinear optimization problems.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.alabama" 

	version("1.0-2", md5="ab1d149ced58a8dbf9fd4ada350dabb8")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-alabama@1.0.1:", type=("build", "run"))
