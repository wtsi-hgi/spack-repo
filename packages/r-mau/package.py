# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMau(RPackage):
	"""Decision Models with Multi Attribute Utility Theory

	Provides functions for the creation, evaluation and test of decision models based in
    Multi Attribute Utility Theory (MAUT). Can process and evaluate local risk aversion utilities
    for a set of indexes, compute utilities and weights for the whole decision tree defining the
    decision model and simulate weights employing Dirichlet distributions under addition constraints 
    in weights.
	"""
	
	homepage = "https://github.com/pedroguarderas/mau"
	cran = "mau" 

	version("0.1.2", md5="8fa0691fb185aadc52257fa3a959384f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
