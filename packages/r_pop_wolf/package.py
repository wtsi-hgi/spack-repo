# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopWolf(RPackage):
	"""Models for Simulating Wolf Populations

	Simulate the dynamic of wolf populations using a specific Individual-Based Model (IBM) compiled in C, see Chapron et al. (2016) <doi:10.1016/j.ecolmodel.2016.08.012>. 
	"""
	
	cran = "pop.wolf" 

	version("1.0", md5="ff27d24fd2f29f47033750f44d3b146a")

	depends_on("r-abind", type=("build", "run"))
