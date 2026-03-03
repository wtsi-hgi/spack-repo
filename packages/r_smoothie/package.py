# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothie(RPackage):
	"""Two-Dimensional Field Smoothing

	Perform two-dimensional smoothing for spatial fields using FFT and the convolution theorem (see Gilleland 2013, <doi:10.5065/D61834G2>).
	"""
	
	homepage = "https://ral.ucar.edu/staff/ericg/"
	cran = "smoothie" 

	version("1.0-3", md5="55e5de4a42d4e85033840cb9734b6572")

	depends_on("r@3:", type=("build", "run"))
