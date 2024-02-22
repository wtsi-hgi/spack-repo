# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubpathwaylnce(RPackage):
	"""Identify Signal Subpathways Competitively Regulated by LncRNAs
Based on ceRNA Theory

	Identify dysfunctional subpathways competitively regulated by lncRNAs through integrating lncRNA-mRNA expression profile and pathway topologies. 
	"""
	
	cran = "SubpathwayLNCE" 

	version("1.0", md5="a696f27c14df4e448f6ef0a6c95714a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
