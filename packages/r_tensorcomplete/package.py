# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorcomplete(RPackage):
	"""Tensor Noise Reduction and Completion Methods

	Efficient algorithms for tensor noise reduction and completion. This package includes a suite of parametric and nonparametric tools for estimating tensor signals from noisy, possibly incomplete observations. The methods allow a broad range of data types, including continuous, binary, and ordinal-valued tensor entries. The algorithms employ the alternating optimization. The detailed algorithm description can be found in the following three references.
	"""
	
	homepage = "Chanwoo"
	cran = "TensorComplete" 

	version("0.2.0", md5="3836c3c5d6b5f2143deaebb1310b95b7")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tensorregress", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
