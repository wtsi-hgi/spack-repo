# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqnet(RPackage):
	"""Log-Linear Poisson Graphical Model with Hot-Deck Multiple
Imputation

	Infer log-linear Poisson Graphical Model with an auxiliary data
    set. Hot-deck multiple imputation method is used to improve the reliability
    of the inference with an auxiliary dataset. Standard log-linear Poisson 
    graphical model can also be used for the inference and the Stability 
    Approach for Regularization Selection (StARS) is implemented to drive the 
    selection of the regularization parameter. The method is fully described in
    <doi:10.1093/bioinformatics/btx819>.
	"""
	
	cran = "RNAseqNet" 

	version("0.1.5", md5="25ca61ec6dffbda643bc7681d57fc8d9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-hot-deck", type=("build", "run"))
	depends_on("r-poiclaclu", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
