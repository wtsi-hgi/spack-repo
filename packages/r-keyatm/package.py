# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyatm(RPackage):
	"""Keyword Assisted Topic Models

	Fits keyword assisted topic models (keyATM) using collapsed Gibbs samplers. The keyATM combines the latent dirichlet allocation (LDA) models with a small number of keywords selected by researchers in order to improve the interpretability and topic classification of the LDA. The keyATM can also incorporate covariates and directly model time trends. The keyATM is proposed in Eshima, Imai, and Sasaki (2023) <doi:10.1111/ajps.12779>.
	"""
	
	homepage = "https://keyatm.github.io/keyATM/"
	cran = "keyATM" 

	version("0.5.1", md5="41192357a3971cab992223994115c75e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-fs@1.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixnormal@0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pgdraw", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-quanteda@3.3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
