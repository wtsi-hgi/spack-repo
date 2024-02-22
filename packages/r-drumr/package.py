# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrumr(RPackage):
	"""Turn R into a Drum Machine

	Includes various functions for playing drum sounds. beat() plays a drum sound
  from one of the six included drum kits. tempo() sets spacing between calls to beat()
  in bpm. Together the two functions can be used to create many different drum patterns. 
	"""
	
	cran = "drumr" 

	version("0.1.0", md5="e92cd93327d6e60f996149b712d1a526")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-audio", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
