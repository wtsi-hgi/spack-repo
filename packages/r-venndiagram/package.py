# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RVenndiagram(RPackage):
	"""Generate High-Resolution Venn and Euler Plots

	A set of functions to generate high-resolution Venn and Euler plots. Includes handling for several special cases, including two-case scaling, and extensive customization of plot shape and structure.
	"""
	
	cran = "VennDiagram" 

	version("1.7.3", md5="aacd2b2f97a705dba364e9b70704ad27")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
