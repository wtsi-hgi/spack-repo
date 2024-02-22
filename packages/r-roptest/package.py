# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoptest(RPackage):
	"""Optimally Robust Estimation

	R infrastructure for optimally robust estimation in general smoothly
            parameterized models using S4 classes and methods as decribed Kohl, M.,
            Ruckdeschel, P., and Rieder, H. (2010), <doi:10.1007/s10260-010-0133-0>, and in
            Rieder, H., Kohl, M., and Ruckdeschel, P. (2008), <doi:10.1007/s10260-007-0047-7>.
	"""
	
	homepage = "http://robast.r-forge.r-project.org/"
	cran = "ROptEst" 

	version("1.3.3", md5="ea98a8230ef4ecc204b321c69e2e8b70")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-distrmod@2.8.1:", type=("build", "run"))
	depends_on("r-randvar@1.2:", type=("build", "run"))
	depends_on("r-robastbase@1.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
