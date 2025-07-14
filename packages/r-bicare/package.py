# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBicare(RPackage):
	"""Biclustering Analysis and Results Exploration

	Biclustering Analysis and Results Exploration.
	"""
	
	homepage = "http://bioinfo.curie.fr"
	bioc = "BicARE"

	version("1.66.0", commit="cb2560664eff0620ac24c5e2dc9d9c7f073581e8")
	version("1.60.0", commit="be7cb92fa2926e99f1e0a27ee6e3cefe8947bb07")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
