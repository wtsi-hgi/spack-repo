# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWfg(RPackage):
	"""Weighted Fast Greedy Algorithm

	Implementation of Weighted Fast Greedy algorithm for community detection in networks with mixed types of attributes.
	"""
	
	cran = "wfg" 

	version("0.1", md5="3a414b2ab114adfe81f900bcedd60ed0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
