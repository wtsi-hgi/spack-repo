# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAudio(RPackage):
	"""Audio Interface for R

	Interfaces to audio devices (mainly sample-based) from R to allow recording and playback of audio. Built-in devices include Windows MM, Mac OS X AudioUnits and PortAudio (the last one is very experimental).
	"""
	
	homepage = "http://www.rforge.net/audio/"
	cran = "audio" 

	version("0.1-11", md5="738a0f33512b741cd991b3a973fb9f64")

	depends_on("r@2:", type=("build", "run"))
