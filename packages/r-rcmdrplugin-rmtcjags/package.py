# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginRmtcjags(RPackage):
	"""R MTC Jags 'Rcmdr' Plugin

	Mixed Treatment Comparison is a methodology to compare directly and/or indirectly health strategies (drugs, treatments, devices). This package provides an 'Rcmdr' plugin to perform Mixed Treatment Comparison for binary outcome using BUGS code from Bristol University (Lu and Ades).
	"""
	
	cran = "RcmdrPlugin.RMTCJags" 

	version("1.0-2", md5="93f38766bfa639013f54357a0a331592")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcmdr@2:", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags@3.0.0:", type=("build", "link", "run"))
