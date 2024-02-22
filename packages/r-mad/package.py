# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMad(RPackage):
	"""Meta-Analysis with Mean Differences

	A collection of functions for conducting a meta-analysis with mean differences data.  It uses recommended procedures as	described in The 	Handbook of Research Synthesis and Meta-Analysis	(Cooper, Hedges, & Valentine, 2009). 
	"""
	
	homepage = "https://www.acdelre.com"
	cran = "MAd" 

	version("0.8-3", md5="3a6951de8f5e5037dd33b39d3dd47f16")

	depends_on("r@2.10.1:", type=("build", "run"))
