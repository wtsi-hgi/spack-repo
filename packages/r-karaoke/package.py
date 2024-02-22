# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaraoke(RPackage):
	"""Remove Vocals from a Song

	Attempts to remove vocals from a stereo '.wav' recording of a song.            
	"""
	
	cran = "karaoke" 

	version("2.0", md5="4a69515c5dcff5efad9fe1164656f645")

	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
