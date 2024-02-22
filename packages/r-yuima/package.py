# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYuima(RPackage):
	"""The YUIMA Project Package for SDEs

	Simulation and Inference for SDEs and Other Stochastic Processes.
	"""
	
	homepage = "https://yuimaproject.com"
	cran = "yuima" 

	version("1.15.22", md5="7110e3334fcc092055c48bbdb782e2bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-boot@1.3.2:", type=("build", "run"))
	depends_on("r-glassofast", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-calculus@0.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
