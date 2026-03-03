# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeras3(RPackage):
	"""R Interface to 'Keras'

	Interface to 'Keras' <https://keras.io>, a high-level neural
  networks API. 'Keras' was developed with a focus on enabling fast experimentation,
  supports both convolution based networks and recurrent networks (as well as
  combinations of the two), and runs seamlessly on both CPU and GPU devices.
	"""
	
	homepage = "https://keras.posit.co/"
	cran = "keras3" 

	version("0.1.0", md5="17cbff0f1004a05644639dd582f0435c", url="https://cran.r-project.org/src/contrib/keras3_0.1.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-generics@0.0.1:", type=("build", "run"))
	depends_on("r-reticulate@1.35:", type=("build", "run"))
	depends_on("r-tensorflow@2.15:", type=("build", "run"))
	depends_on("r-tfruns@1.5.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
