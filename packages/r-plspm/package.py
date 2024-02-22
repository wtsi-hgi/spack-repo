# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlspm(RPackage):
	"""Partial Least Squares Path Modeling (PLS-PM)

	Partial Least Squares Path Modeling (PLS-PM), Tenenhaus, Esposito Vinzi, Chatelin, Lauro (2005) <doi:10.1016/j.csda.2004.03.005>,
    analysis for both metric and non-metric data, as well as REBUS analysis, Esposito Vinzi, Trinchera, Squillacciotti, and Tenenhaus (2008) <doi:10.1002/asmb.728>.
	"""
	
	homepage = "https://github.com/gastonstat/plspm"
	cran = "plspm" 

	version("0.5.1", md5="25bf4e91b5e93aeacf91a3de17ab24f4")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-tester", type=("build", "run"))
	depends_on("r-turner", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
