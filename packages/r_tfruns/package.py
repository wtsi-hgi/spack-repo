# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfruns(RPackage):
	"""Training Run Tools for 'TensorFlow'

	Create and manage unique directories for each 'TensorFlow' 
  training run. Provides a unique, time stamped directory for each run
  along with functions to retrieve the directory of the latest run or 
  latest several runs. 
	"""
	
	homepage = "https://github.com/rstudio/tfruns"
	cran = "tfruns" 

	version("1.5.2", md5="8325a9f1081ab8a010cad6774a2b2c4f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.2:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
