# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiogrowth(RPackage):
	"""Modelling of Population Growth

	Modelling of population growth under static and dynamic environmental conditions. 
    Includes functions for model fitting and making prediction under isothermal and 
    dynamic conditions. The methods (algorithms & models) are based on
    predictive microbiology (See Perez-Rodriguez and Valero (2012, ISBN:978-1-4614-5519-6)).
	"""
	
	cran = "biogrowth" 

	version("1.0.3", md5="670bef929f0afae02fa9fbf06d547e71")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-desolve@1.28:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-fme@1.3.6:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-cowplot@1:", type=("build", "run"))
	depends_on("r-lamw@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-formula-tools@1.7.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
