# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidylda(RPackage):
	"""Latent Dirichlet Allocation Using 'tidyverse' Conventions

	Implements an algorithm for Latent Dirichlet
    Allocation (LDA), Blei et at. (2003) <https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf>,
    using style conventions from the 'tidyverse',
    Wickham et al. (2019)<doi:10.21105/joss.01686>,
    and 'tidymodels', Kuhn et al.<https://tidymodels.github.io/model-implementation-principles/>.
    Fitting is done via collapsed Gibbs sampling.
    Also implements several novel features for LDA such as guided models and
    transfer learning based on ongoing and, as yet, unpublished research.
	"""
	
	homepage = "https://github.com/TommyJones/tidylda/"
	cran = "tidylda" 

	version("0.0.4", md5="30c5c2f58f7068fff502499849674efa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvrsquared@0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
