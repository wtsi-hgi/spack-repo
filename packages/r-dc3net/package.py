# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDc3net(RPackage):
	"""Inferring Condition-Specific Networks via Differential Network
Inference

	Performs differential network analysis to infer disease specific gene networks.
	"""
	
	cran = "dc3net" 

	version("1.2.0", md5="4aa30ab4d3add2bcdc2551c7e63278e3")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-c3net", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reder", type=("build", "run"))
