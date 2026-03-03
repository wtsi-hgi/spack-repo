# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnnx(RPackage):
	"""R Interface to 'ONNX'

	R Interface to 'ONNX' - Open Neural Network Exchange <https://onnx.ai/>. 
             'ONNX' provides an open source format for machine learning models. 
             It defines an extensible computation graph model, as well as definitions
             of built-in operators and standard data types.
	"""
	
	homepage = "https://github.com/onnx/onnx-r"
	cran = "onnx" 

	version("0.0.3", md5="a25e6b676ec3e64981b6b6261668cddb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-reticulate@1.4:", type=("build", "run"))
