# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundgen(RPackage):
	"""Sound Synthesis and Acoustic Analysis

	Performs parametric synthesis of sounds with harmonic and noise 
    components such as animal vocalizations or human voice. Also offers tools 
    for audio manipulation and acoustic analysis, including pitch tracking, 
    spectral analysis, audio segmentation, pitch and formant shifting, etc. 
    Includes four interactive web apps for synthesizing and annotating audio, 
    manually correcting pitch contours, and measuring formant frequencies. 
    Reference: Anikin (2019) <doi:10.3758/s13428-018-1095-7>.
	"""
	
	homepage = "http://cogsci.se/soundgen.html"
	cran = "soundgen" 

	version("2.6.2", md5="e676daec20cdc1f7201ef2fd095ac5b7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-seewave@2.1.6:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-phontools", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-nonlineartseries", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
