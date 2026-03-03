# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVesselr(RPackage):
	"""Gradient and Vesselness Tools for Arrays and NIfTI Images

	Simple functions for calculating the image gradient, image hessian, volume ratio filter, and Frangi vesselness filter of 3-dimensional volumes.
	"""
	
	homepage = "https://github.com/jdwor/vesselr"
	cran = "vesselr" 

	version("0.2.1", md5="8125e9a8228adc21c43bc04d5332f86a")

	depends_on("r-oro-nifti", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
