# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDavies(RPackage):
	"""The Davies Quantile Function

	Various utilities for the Davies distribution.
	"""
	
	cran = "Davies" 

	version("1.2-0", md5="686f4b640cb952b78b646ed6305d3667")

	depends_on("r-mathjaxr", type=("build", "run"))
