# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSprex(RPackage):
	"""Calculate Species Richness and Extrapolation Metrics

	Calculate species richness functions for rarefaction and
    extrapolation.
	"""
	
	cran = "sprex" 

	version("1.4.1", md5="fc11c1f8e090853af7f9a1829622c611")

	depends_on("r-swfscmisc@1.1:", type=("build", "run"))
