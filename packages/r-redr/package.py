# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedr(RPackage):
	"""REgularization by Denoising (RED)

	Regularization by Denoising uses a denoising engine to solve
  many image reconstruction ill-posed inverse problems. This is a R
  implementation of the algorithm developed by Romano et.al. (2016) <arXiv:1611.02862>. Currently,
  only the gradient descent optimization framework is implemented. Also,
  only the median filter is implemented as a denoiser engine. However,
  (almost) any denoiser engine can be plugged in. There are currently available
  3 reconstruction tasks: denoise, deblur and super-resolution. And again,
  any other task can be easily plugged into the main function 'RED'.
	"""
	
	cran = "redR" 

	version("1.0.1", md5="9416bff9f7e463cff5c6ea69e430a1f7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
