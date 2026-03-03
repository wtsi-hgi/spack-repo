# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginOsqp(RPackage):
	"""'osqp' Plugin for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
         with the quadratic solver 'OSQP'. More information about
         'OSQP' can be found at <https://osqp.org>.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.osqp" 

	version("1.0-1", md5="8feea5eabbf16981c4228ab6fe2f4f19")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-roi@1.0.1:", type=("build", "run"))
	depends_on("r-osqp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
