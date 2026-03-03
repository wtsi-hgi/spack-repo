# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfdatasets(RPackage):
	"""Interface to 'TensorFlow' Datasets

	Interface to 'TensorFlow' Datasets, a high-level library for
    building complex input pipelines from simple, re-usable pieces.
    See <https://www.tensorflow.org/guide> for additional
    details.
	"""
	
	homepage = "https://github.com/rstudio/tfdatasets"
	cran = "tfdatasets" 

	version("2.9.0", md5="9889150ce203c3ca329ed46eeb868de0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reticulate@1.10:", type=("build", "run"))
	depends_on("r-tensorflow@1.13.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("py-tensorflow@1.4:", type=("build", "link", "run"))
