# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCallsync(RPackage):
	"""Recording Synchronisation, Call Detection and Assignment, Audio
Analysis

	Intended to analyse recordings from multiple microphones (e.g., backpack
  microphones in captive setting). It allows users to align recordings even if there is non-linear 
  drift of several minutes between them. A call detection and assignment pipeline can be used 
  to find vocalisations and assign them to the vocalising individuals (even if the vocalisation
  is picked up on multiple microphones). The tracing and measurement functions allow for detailed
  analysis of the vocalisations and filtering of noise. Finally, the package includes a function
  to run spectrographic cross correlation, which can be used to compare vocalisations. It also 
  includes multiple other functions related to analysis of vocal behaviour.
	"""
	
	homepage = "https://github.com/simeonqs/callsync"
	cran = "callsync" 

	version("0.2.1", md5="b441abc2f7845e09c6d16a1265e1d560")
	version("0.0.6", md5="187774f13da627a0f44598514733da1c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-oce@1.7:", type=("build", "run"))
	depends_on("r-seewave@2.2:", type=("build", "run"))
	depends_on("r-signal@0.7:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tuner@1.4:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
