# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtpm(RPackage):
	"""Continuous-Time Phylogenetic Modeling

	Functions for identifying, fitting, and applying continuous-time stochastic models to phylogenetic data.
  The package is based on methods introduced in
  Noonan et al. (2021) <doi:10.1101/2021.05.21.445056>.
	"""
	
	homepage = "https://github.com/NoonanM/ctpm"
	cran = "ctpm" 

	version("1.0.1", md5="15c0b37a5942937d6b2bf00bd4c3d74d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ctmm", type=("build", "run"))
	depends_on("r-slouch", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
