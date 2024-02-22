# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepliscope(RPackage):
	"""Replication Timing Profiling using DNA Copy Number

	Create, Plot and Compare Replication Timing Profiles. The method is described in Muller et al., (2014) <doi: 10.1093/nar/gkt878>.
	"""
	
	cran = "Repliscope" 

	version("1.1.1", md5="e17244e56190d91d1bf7aa09820ee732")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
