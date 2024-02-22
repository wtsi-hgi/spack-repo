# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelcount(RPackage):
	"""Random Effects and/or Sample Selection Models for Panel Count
Data

	A high performance package implementing random effects and/or
    sample selection models for panel count data. The details of the models are discussed in Peng and Van den Bulte (2023) <doi:10.2139/ssrn.2702053>.
	"""
	
	cran = "PanelCount" 

	version("2.0.1", md5="0495d782ee35fabf2a22700ab2fcf4d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
