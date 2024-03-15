# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanter(RPackage):
	"""BioAcoustic eveNT classifiER

	Create a hierarchical acoustic event species classifier out of  
  multiple call type detectors as described in 
  Rankin et al (2017) <doi:10.1111/mms.12381>.
	"""
	
	cran = "banter" 

	version("0.9.6", md5="9fddd386b65aca1e7a5e81254089ecaa")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-randomforest@4.6:", type=("build", "run"))
	depends_on("r-rfpermute@2.5.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-swfscmisc@1.5:", type=("build", "run"))
	depends_on("r-tibble@3.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
