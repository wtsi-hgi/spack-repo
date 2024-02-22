# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveletcomp(RPackage):
	"""Computational Wavelet Analysis

	Wavelet analysis and reconstruction of time series, cross-wavelets and phase-difference (with filtering options), significance with simulation algorithms.
	"""
	
	homepage = "Guide"
	cran = "WaveletComp" 

	version("1.1", md5="f98a5d6a1e8708935239e1dd11646701")

	depends_on("r@2.10:", type=("build", "run"))
