# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmgp(RPackage):
	"""Tools for Modeling ERGM Generating Processes

	Provides tools for simulating draws from continuous time processes with well-defined exponential family random graph (ERGM) equilibria, i.e. ERGM generating processes (EGPs).  A number of EGPs are supported, including the families identified in Butts (2023) <doi:10.1080/0022250X.2023.2180001>, as are functions for hazard calculation and timing calibration.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergmgp" 

	version("0.1-1", md5="bf3ce8d9dc688fb9d49bae03d7b00c6f")

	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-networkdynamic@0.10:", type=("build", "run"))
	depends_on("r-statnet-common@4.2:", type=("build", "run"))
