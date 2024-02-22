# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuner(RPackage):
	"""Analysis of Music and Speech

	Analyze music and speech, extract features like MFCCs, handle wave files and their representation in various ways, read mp3, read midi, perform steps of a transcription, ...
        Also contains functions ported from the 'rastamat' 'Matlab' package.
	"""
	
	cran = "tuneR" 

	version("1.4.6", md5="2cd2209ae89c82980382c53ea90c27c9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
