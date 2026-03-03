# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyindex(RPackage):
	"""A Tidy Data Pipeline to Construct, Compare, and Analyse Indexes

	Construct and analyse indexes in a pipeline tidy workflow.
    'tidyindex' contains modules for transforming variables, aggregating 
    variables across time, reducing data dimension through weighting, and 
    fitting distributions. A manuscript describing the methodology can be 
    found at <https://github.com/huizezhang-sherry/paper-tidyindex>.
	"""
	
	homepage = "https://github.com/huizezhang-sherry/tidyindex"
	cran = "tidyindex" 

	version("0.1.0", md5="20f939b08e8f6f4f2e525a1c96976d1d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
