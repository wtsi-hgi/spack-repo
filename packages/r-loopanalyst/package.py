# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoopanalyst(RPackage):
	"""A Collection of Tools to Conduct Levins' Loop Analysis

	Loop analysis makes qualitative predictions of variable change in a system of causally interdependent variables, where "qualitative" means sign only (i.e. increases, decreases, non change, and ambiguous). This implementation includes output support for graphs in .dot file format for use with visualization software such as 'graphviz' (<http://graphviz.org>). 'LoopAnalyst' provides tools for the construction and output of community matrices, computation and output of community effect matrices, tables of correlations, adjoint, absolute feedback, weighted feedback and weighted prediction matrices, change in life expectancy matrices, and feedback, path and loop enumeration tools.
	"""
	
	homepage = "https://www.alexisdinno.com/LoopAnalyst"
	cran = "LoopAnalyst" 

	version("1.2-6", md5="ac09953a6fb984851bc023ac3196ca76")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
