# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaved(RPackage):
	"""Wavelet Deconvolution

	Makes available code necessary to reproduce figures and
        tables in papers on the WaveD method for wavelet deconvolution
        of noisy signals as presented in The WaveD Transform in R,
        Journal of Statistical Software Volume 21, No. 3, 2007.
	"""
	
	homepage = "https://www.jstatsoft.org/v21/i02"
	cran = "waved" 

	version("1.3", md5="1554c1dd527e150194892aeb1ecef3e4")

