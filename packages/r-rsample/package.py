# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsample(RPackage):
	"""General Resampling Infrastructure

	Classes and functions to create and summarize different types
    of resampling objects (e.g. bootstrap, cross-validation).
	"""
	
	homepage = "https://rsample.tidymodels.org"
	cran = "rsample" 

	version("1.2.0", md5="2cb8f420de59388f36051416726c21d9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-slider@0.1.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
