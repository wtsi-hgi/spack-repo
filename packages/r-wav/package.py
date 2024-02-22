# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWav(RPackage):
	"""Read and Write WAV Files

	Efficiently read and write Waveform (WAV) audio files <https://en.wikipedia.org/wiki/WAV>. 
  Support for unsigned 8 bit Pulse-code modulation (PCM), signed 12, 16, 24 and 32 bit 
  PCM and other encodings.  
	"""
	
	homepage = "https://github.com/mlverse/wav"
	cran = "wav" 

	version("0.1.0", md5="33937e44a382c6362093a3f582714e20")

	depends_on("r-rcpp", type=("build", "run"))
