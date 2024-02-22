# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhosa(RPackage):
	"""Higher-Order Spectral Analysis

	Higher-order spectra or polyspectra of time series, such as bispectrum and bicoherence, have been investigated in abundant literature and applied to problems of signal detection in a wide range of fields. This package aims to provide a simple API to estimate and analyze them. The current implementation is based on Brillinger and Irizarry (1998) <doi:10.1016/S0165-1684(97)00217-X> for estimating bispectrum or bicoherence, Lii and Helland (1981) <doi:10.1145/355958.355961> for cross-bispectrum, and Kim and Powers (1979) <doi:10.1109/TPS.1979.4317207> for cross-bicoherence.
	"""
	
	homepage = "https://tabe.github.io/rhosa/"
	cran = "rhosa" 

	version("0.2.0", md5="3c2439fbd53d994843ce6823a310936f")

