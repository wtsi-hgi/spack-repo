# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemodecomp(RPackage):
	"""Decompose Demographic Functions

	Two general demographic decomposition methods are offered: Pseudo-continuous decomposition proposed by Horiuchi, Wilmoth, and Pletcher (2008) <doi:10.1353/dem.0.0033> and stepwise replacement decomposition proposed by Andreev, Shkolnikov and Begun (2002) <doi:10.4054/DemRes.2002.7.14>.
	"""
	
	cran = "DemoDecomp" 

	version("1.0.1", md5="2aee0a516c976bb1ac047ccb41943ced")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
