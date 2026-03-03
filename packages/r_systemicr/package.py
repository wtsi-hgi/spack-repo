# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystemicr(RPackage):
	"""Monitoring Systemic Risk

	The past decade has demonstrated an increased need to better understand risks leading to systemic crises. This framework offers scholars, practitioners and policymakers a useful toolbox to explore such risks in financial systems. Specifically, this framework provides popular econometric and network measures to monitor systemic risk and to measure the consequences of regulatory decisions. These systemic risk measures are based on the frameworks of Adrian and Brunnermeier (2016) <doi:10.1257/aer.20120555> and Billio, Getmansky, Lo and Pelizzon (2012) <doi:10.1016/j.jfineco.2011.12.010>.
	"""
	
	cran = "SystemicR" 

	version("0.1.0", md5="cc4ed2885188e02a74f29f00a6c77fa2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
