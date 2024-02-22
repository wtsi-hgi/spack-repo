# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeras(RPackage):
	"""R Interface to 'Keras'

	Interface to 'Keras' <https://keras.io>, a high-level neural
  networks 'API'. 'Keras' was developed with a focus on enabling fast experimentation,
  supports both convolution based networks and recurrent networks (as well as
  combinations of the two), and runs seamlessly on both 'CPU' and 'GPU' devices.
	"""
	
	homepage = "https://tensorflow.rstudio.com/"
	cran = "keras" 

	version("2.13.0", md5="2b8c9d8eb5f49097efb97e63796690fd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-generics@0.0.1:", type=("build", "run"))
	depends_on("r-reticulate@1.31:", type=("build", "run"))
	depends_on("r-tensorflow@2.8:", type=("build", "run"))
	depends_on("r-tfruns@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
