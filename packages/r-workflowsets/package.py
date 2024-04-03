# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorkflowsets(RPackage):
	"""Create a Collection of 'tidymodels' Workflows

	A workflow is a combination of a model and preprocessors
    (e.g, a formula, recipe, etc.) (Kuhn and Silge (2021)
    <https://www.tmwr.org/>). In order to try different combinations of
    these, an object can be created that contains many workflows. There
    are functions to create workflows en masse as well as training them
    and visualizing the results.
	"""
	
	homepage = "https://github.com/tidymodels/workflowsets"
	cran = "workflowsets" 

	version("1.1.0", md5="7b34448c75c79c386e702a3e0ea1385b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat@1.2:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-parsnip@1.2:", type=("build", "run"))
	depends_on("r-pillar@1.7:", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-rsample@0.0.9:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tune@1.2:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-workflows@1.1.4:", type=("build", "run"))
