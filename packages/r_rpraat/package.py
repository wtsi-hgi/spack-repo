# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpraat(RPackage):
	"""Interface to Praat

	Read, write and manipulate 'Praat' TextGrid, PitchTier, Pitch, IntensityTier, Formant, Sound, and Collection files <https://www.fon.hum.uva.nl/praat/>.
	"""
	
	homepage = "https://github.com/bbTomas/rPraat/"
	cran = "rPraat" 

	version("1.3.2-1", md5="6e01a875d321eeef26cff546a249f802")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.6:", type=("build", "run"))
	depends_on("r-tuner@1.3.3:", type=("build", "run"))
