# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtfhplus(RPackage):
	"""Implementation of LT-FH++

	Implementation of LT-FH++, an extension of
    the liability threshold family history (LT-FH) model.
    LT-FH++ uses a Gibbs sampler for sampling from the truncated 
    multivariate normal distribution and allows for 
    flexible family structures. LT-FH++ was first described in 
    Pedersen, Emil M., et al. (2022) 
    <https://pure.au.dk/ws/portalfiles/portal/353346245/> 
    as an extension to LT-FH with more flexible family structures, 
    and again as the age-dependent liability threshold (ADuLT) model
    Pedersen, Emil M., et al. (2023) 
    <https://www.nature.com/articles/s41467-023-41210-z> 
    as an alternative to traditional time-to-event genome-wide
    association studies, where family history was not considered.
	"""
	
	homepage = "https://github.com/EmilMiP/LTFHPlus"
	cran = "LTFHPlus" 

	version("2.1.1", md5="5fa1c1561144a1859d188573e2287ac7")

	depends_on("r-batchmeans", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
