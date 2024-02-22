# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgua(RPackage):
	"""'tidymodels' Integration with 'h2o'

	Create and evaluate models using 'tidymodels' and 'h2o' <https://h2o.ai/>. The
    package enables users to specify 'h2o' as an engine for several
    modeling methods.
	"""
	
	homepage = "https://agua.tidymodels.org/"
	cran = "agua" 

	version("0.1.3", md5="6ba5d4740578e7269cffb690bf32cc65")

	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics@0.1.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-h2o@3.38.0.1:", type=("build", "run"))
	depends_on("r-hardhat@1.1:", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tune@1.0.1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
