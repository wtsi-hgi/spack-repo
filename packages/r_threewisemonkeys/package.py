# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreewisemonkeys(RPackage):
	"""The Japanese Pictorial Maxim "See No Evil, Hear No Evil, Speak
No Evil"

	Does nothing useful, but perhaps does that nothing in an entertaining or informative fashion.
	"""
	
	cran = "ThreeWiseMonkeys" 

	version("0.1.0", md5="4a40b76c1a7e301e2340601be42b4aa1")

	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
