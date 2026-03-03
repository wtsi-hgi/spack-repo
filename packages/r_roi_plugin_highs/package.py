# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginHighs(RPackage):
	"""'HiGHS' Plugin for the 'R' Optimization Infrastructure

	Enhances the 'R' Optimization Infrastructure ('ROI') package
         with the quadratic solver 'HiGHS'. More information about
         'HiGHS' can be found at <https://highs.dev>.
	"""
	
	cran = "ROI.plugin.highs" 

	version("1.0-3", md5="4cbd466db6b32596a03cdf36426b98f0")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-highs", type=("build", "run"))
