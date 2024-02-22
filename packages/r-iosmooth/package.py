# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIosmooth(RPackage):
	"""Functions for Smoothing with Infinite Order Flat-Top Kernels

	Density, spectral density, and regression estimation using infinite
    order flat-top kernels.
	"""
	
	cran = "iosmooth" 

	version("0.94", md5="5cf641db20c380dd3d3d1201e4ed26ae")

