# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGofkernel(RPackage):
	"""Testing Goodness-of-Fit with the Kernel Density Estimator

	Tests of goodness-of-fit based on a kernel smoothing of the data.
	"""
	
	cran = "GoFKernel" 

	version("2.1-1", md5="2874ad08b0f92ea2f286e1f812881755")

	depends_on("r-kernsmooth", type=("build", "run"))
