# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginTeachingdemos(RPackage):
	"""Rcmdr Teaching Demos Plug-in

	Provides an Rcmdr "plug-in" based on the TeachingDemos package, and is primarily for illustrative purposes.
	"""
	
	cran = "RcmdrPlugin.TeachingDemos" 

	version("1.2-0", md5="001a250abf96aeed05e2ca4a28b3d411")

	depends_on("r-teachingdemos@2.9:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
