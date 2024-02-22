# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfestimators(RPackage):
	"""Interface to 'TensorFlow' Estimators

	Interface to 'TensorFlow' Estimators 
    <https://www.tensorflow.org/guide/estimator>, a high-level 
    API that provides implementations of many different model types 
    including linear models and deep neural networks. 
	"""
	
	homepage = "https://github.com/rstudio/tfestimators"
	cran = "tfestimators" 

	version("1.9.2", md5="4a9432c5618430024e57418dc4faa387")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-forge", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-reticulate@1.10:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tensorflow@1.9:", type=("build", "run"))
	depends_on("r-tfruns@1.1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
