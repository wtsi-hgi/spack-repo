# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusic(RPackage):
	"""Learn and Experiment with Music Theory

	An aid for learning and using music theory. You can build chords, scales, and chord progressions using 12-note equal temperament tuning (12-ET) or user-defined tuning. Includes functions to visualize notes on a piano using ASCII plots in the console and to plot waveforms using base graphics. It allows simple playback of notes and chords using the 'audio' package.
	"""
	
	homepage = "https://github.com/egenn/music"
	cran = "music" 

	version("0.1.2", md5="3a6e81786ad8bad2c5ec1cecaf6f6e32")

	depends_on("r-audio", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
