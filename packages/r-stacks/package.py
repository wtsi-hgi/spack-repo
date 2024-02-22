# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStacks(RPackage):
	"""Tidy Model Stacking

	Model stacking is an ensemble technique that involves
    training a model to combine the outputs of many diverse statistical
    models, and has been shown to improve predictive performance in a
    variety of settings. 'stacks' implements a grammar for
    'tidymodels'-aligned model stacking.
	"""
	
	homepage = "https://stacks.tidymodels.org/"
	cran = "stacks" 

	version("1.0.3", md5="8d60c355c782ad5dc16432fe2bd149b9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-butcher@0.1.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-parsnip@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-recipes@0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-rsample@0.1.1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tune@0.1.3:", type=("build", "run"))
	depends_on("r-vctrs@0.6.1:", type=("build", "run"))
	depends_on("r-workflows@0.2.3:", type=("build", "run"))
	depends_on("r-yardstick@1.1:", type=("build", "run"))
