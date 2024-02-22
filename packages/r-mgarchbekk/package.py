# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgarchbekk(RPackage):
	"""Simulating, Estimating and Diagnosing MGARCH (BEKK and mGJR)
Processes

	Procedures to simulate, estimate and diagnose MGARCH
    processes of BEKK and multivariate GJR (bivariate asymmetric GARCH
    model) specification.
	"""
	
	homepage = "https://github.com/vst/mgarchBEKK/"
	cran = "mgarchBEKK" 

	version("0.0.5", md5="3fc55494768531eb387dded60c92450d")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
