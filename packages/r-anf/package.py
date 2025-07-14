# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnf(RPackage):
	"""Affinity Network Fusion for Complex Patient Clustering

	This package is used for complex patient clustering by integrating multi-omic data through affinity network fusion.
	"""
	
	bioc = "ANF"

	version("1.30.0", commit="8b423c0f7828f27bfbac13fd6d915f9b747fad78")
	version("1.24.1", commit="360f3cd6794197b719d56f0c76587d61a47ecb3f")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
