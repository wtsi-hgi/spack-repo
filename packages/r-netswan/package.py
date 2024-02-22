# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetswan(RPackage):
	"""Network Strengths and Weaknesses Analysis

	A set of functions for studying network robustness, resilience and vulnerability. 
	"""
	
	cran = "NetSwan" 

	version("0.1", md5="a378149f54bd0a58c5616c1c0f881c78")

	depends_on("r-igraph", type=("build", "run"))
