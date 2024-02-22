# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTorchvisionlib(RPackage):
	"""Additional Operators for Image Models

	Implements additional operators for computer vision models, including
    operators necessary for image segmentation and object detection deep learning
    models.
	"""
	
	homepage = "https://github.com/mlverse/torchvisionlib"
	cran = "torchvisionlib" 

	version("0.5.0", md5="dbc13d10456147e666954c71aafe45dc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
