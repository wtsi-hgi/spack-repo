# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLavasearch2(RPackage):
	"""Tools for Model Specification in the Latent Variable Framework

	Tools for model specification in the latent variable framework
    (add-on to the 'lava' package). The package contains three main functionalities:
    Wald tests/F-tests with improved control of the type 1 error in small samples,
    adjustment for multiple comparisons when searching for local dependencies,
    and adjustment for multiple comparisons when doing inference for multiple latent variable models. 
	"""
	
	homepage = "https://github.com/bozenne/lavaSearch2"
	cran = "lavaSearch2" 

	version("2.0.2", md5="9b1140c93438cf36c09edd8bedb98c58", url="https://cran.r-project.org/src/contrib/lavaSearch2_2.0.2.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lava@1.6.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
