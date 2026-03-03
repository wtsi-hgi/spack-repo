# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImbibe(RPackage):
	"""A Pipe-Friendly Image Calculator

	Provides a set of fast, chainable image-processing operations
             which are applicable to images of two, three or four dimensions,
             particularly medical images.
	"""
	
	homepage = "https://github.com/jonclayden/imbibe"
	cran = "imbibe" 

	version("0.1.1", md5="a233db03a2c99de3cae7cdc14aa41e34")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
