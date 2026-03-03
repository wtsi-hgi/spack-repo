# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhnr(RPackage):
	"""An Implementation of the Artificial Hydrocarbon Networks

	Implementation of the Artificial Hydrocarbon Networks for data
    modeling.
	"""
	
	homepage = "https://github.com/jroberayalas/ahnr"
	cran = "ahnr" 

	version("0.3.1", md5="502246a7c8bc063d825770c82646519f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
