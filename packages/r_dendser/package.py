# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendser(RPackage):
	"""Dendrogram Seriation: Ordering for Visualisation

	Re-arranges a dendrogram to optimize visualisation-based cost functions.
	"""
	
	cran = "DendSer" 

	version("1.0.2", md5="d28c7b5b367520cfa213a45f5b9c77d9")

	depends_on("r-gclus", type=("build", "run"))
	depends_on("r-seriation", type=("build", "run"))
