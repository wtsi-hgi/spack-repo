# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynchwave(RPackage):
	"""Synchrosqueezed Wavelet Transform

	The synchrosqueezed wavelet transform is implemented. The package is a translation of MATLAB Synchrosqueezing Toolbox, version 1.1 originally developed by Eugene Brevdo (2012). The C code for curve_ext was authored by Jianfeng Lu, and translated to Fortran by Dongik Jang. Synchrosqueezing is based on the papers: [1] Daubechies, I., Lu, J. and Wu, H. T. (2011) Synchrosqueezed wavelet transforms: An empirical mode decomposition-like tool. Applied and Computational Harmonic Analysis, 30. 243-261. [2] Thakur, G., Brevdo, E., Fukar, N. S. and Wu, H-T. (2013) The Synchrosqueezing algorithm for time-varying spectral analysis: Robustness properties and new paleoclimate applications. Signal Processing, 93, 1079-1094.
	"""
	
	cran = "SynchWave" 

	version("1.1.2", md5="069429b1140b25fc5d2e39e0e115f4ea")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-fields@6.7.6:", type=("build", "run"))
