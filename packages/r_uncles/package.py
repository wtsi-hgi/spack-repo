# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncles(RPackage):
	"""Unification of Clustering Results from Multiple Datasets using
External Specifications

	Consensus clustering by the unification of clustering results from multiple datasets using external specifications.
	"""
	
	cran = "UNCLES" 

	version("2.0", md5="2b6c593ed83200f0c90fdc18bf47dafb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
