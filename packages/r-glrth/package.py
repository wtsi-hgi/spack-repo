# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlrth(RPackage):
	"""Genome-Wide Association and Linkage Analysis under Heterogeneity

	Likelihood ratio tests for genome-wide association and genome-wide linkage analysis under heterogeneity. 
	"""
	
	cran = "gLRTH" 

	version("0.2.0", md5="4ba3c6ff5ebfddab967ab5fb037c4a19")

	depends_on("r@3.4:", type=("build", "run"))
