# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpaa(RPackage):
	"""SPecies Association Analysis

	Miscellaneous functions for analysing species association
        and niche overlap.
	"""
	
	homepage = "https://github.com/helixcn/spaa"
	cran = "spaa" 

	version("0.2.2", md5="129371cf0d3212cfc06152660606c5de")

