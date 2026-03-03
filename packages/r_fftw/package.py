# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFftw(RPackage):
	"""Fast FFT and DCT Based on the FFTW Library

	Provides a simple and efficient wrapper around the fastest
        Fourier transform in the west (FFTW) library <http://www.fftw.org/>.
	"""
	
	cran = "fftw" 

	version("1.0-8", md5="7616d850e0f1256f89031b7f2c5a592c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
