# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfio(RPackage):
	"""Interface to 'TensorFlow IO'

	Interface to 'TensorFlow IO', Datasets and filesystem extensions maintained by `TensorFlow SIG-IO` <https://github.com/tensorflow/community/blob/master/sigs/io/CHARTER.md>.
	"""
	
	homepage = "https://github.com/tensorflow/io"
	cran = "tfio" 

	version("0.4.1", md5="59e9161656495989156370781f4c4198")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reticulate@1.10:", type=("build", "run"))
	depends_on("r-tensorflow@1.9:", type=("build", "run"))
	depends_on("r-tfdatasets@1.9:", type=("build", "run"))
	depends_on("r-forge", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("py-tensorflow@1.13.0:", type=("build", "link", "run"))
