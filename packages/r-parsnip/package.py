# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsnip(RPackage):
	"""A Common API to Modeling and Analysis Functions

	A common interface is provided to allow users to specify a
    model without having to remember the different argument names across
    different functions or computational engines (e.g. 'R', 'Spark',
    'Stan', 'H2O', etc).
	"""
	
	homepage = "https://github.com/tidymodels/parsnip"
	cran = "parsnip" 

	version("1.2.1", md5="8963904d37b6296869d29d0a8c22e61a")
	version("1.2.0", md5="5511bd877b251ff068613fd7e47d387c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat@1.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
