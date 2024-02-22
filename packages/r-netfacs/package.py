# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetfacs(RPackage):
	"""Network Applications to Facial Communication Data

	Functions to analyze and visualize communication data, 
      based on network theory and resampling methods. 
      Farine, D. R. (2017) <doi:10.1111/2041-210X.12772>;
      Carsey, T., & Harden, J. (2014) <doi:10.4135/9781483319605>.
      Primarily targeted at datasets of facial expressions coded with the Facial Action Coding System. 
      Ekman, P., Friesen, W. V., & Hager, J. C. (2002). "Facial action coding system - investigator's guide" <https://www.paulekman.com/facial-action-coding-system/>.
	"""
	
	cran = "NetFACS" 

	version("0.5.0", md5="a2d65b335ac606b941267396e44b1fac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
