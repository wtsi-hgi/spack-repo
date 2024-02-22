# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHotspot(RPackage):
	"""Software Hotspot Analysis

	Contains data for software hotspot analysis, along with a function performing the analysis itself.
	"""
	
	cran = "hotspot" 

	version("1.0", md5="513ec4cdcd57f2391f70805ffc66a119")

