# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimatrends(RPackage):
	"""Climate Variability Indices for Ecological Modelling

	Supports analysis of trends in climate change,
        ecological and crop modelling.
	"""
	
	homepage = "https://agrdatasci.github.io/climatrends/"
	cran = "climatrends" 

	version("0.5", md5="2d50debb7cac07f7b596304d9007c2c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nasapower", type=("build", "run"))
