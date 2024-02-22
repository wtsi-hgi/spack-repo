# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKza(RPackage):
	"""Kolmogorov-Zurbenko Adaptive Filters

	Time Series Analysis including break detection, spectral analysis, KZ Fourier Transforms.
	"""
	
	cran = "kza" 

	version("4.1.0.1", md5="8507fade15e40f1b036858e0dda434c8")

	depends_on("fftw@3.2.2:", type=("build", "link", "run"))
