# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamic(RPackage):
	"""DFI Cutoffs for Latent Variable Models

	Returns dynamic fit index (DFI) cutoffs for latent variable models 
    that are tailored to the user's model statement, model type, and sample size.  
    This is the counterpart of the Shiny Application, <https://dynamicfit.app>.
	"""
	
	homepage = "https://github.com/melissagwolf/dynamic"
	cran = "dynamic" 

	version("1.1.0", md5="e830766b44eb42a7fcd07a0c132cb606")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-simstandard@0.6.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-lavaan@0.6.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-patchwork@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
