# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysdm(RPackage):
	"""Species Distribution Models with Tidymodels

	Fit species distribution models (SDMs) using the 'tidymodels' framework, 
  which provides a standardised interface to define models and process their 
  outputs. 'tidysdm' expands 'tidymodels' by providing methods for spatial objects,
  as well as a number of specialised functions to process presences and pseudoabsences
  for contemporary and palaeo datasets. The full 
  functionalities of the package are described
  in Leonardi et al. (2023) <doi:10.1101/2023.07.24.550358>.
	"""
	
	homepage = "https://github.com/EvolEcolGroup/tidysdm"
	cran = "tidysdm" 

	version("0.9.4", md5="5032958d0b3ca5a68e048ee838a490a3")

	depends_on("r-tidymodels", type=("build", "run"))
	depends_on("r-spatialsample", type=("build", "run"))
	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-dalextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maxnet", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
