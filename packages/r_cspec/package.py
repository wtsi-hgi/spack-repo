# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCspec(RPackage):
	"""Complete Discrete Fourier Transform (DFT) and Periodogram

	Calculate the predictive discrete Fourier transform, complete discrete Fourier transform, complete periodogram, and tapered complete periodogram. This algorithm is based on the preprint "Spectral methods for small sample time series: A complete periodogram approach" (2020) by Sourav Das, Suhasini Subba Rao, and Junho Yang.
	"""
	
	cran = "cspec" 

	version("0.1.2", md5="0ee840608fdb516f271c0232373e7a2f")

