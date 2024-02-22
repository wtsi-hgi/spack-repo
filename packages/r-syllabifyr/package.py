# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyllabifyr(RPackage):
	"""Syllabifier for CMU Dictionary Transcriptions

	Implements tidy syllabification of transcription. 
  Based on @kylebgorman's 'python' implementation <https://github.com/kylebgorman/syllabify>.
	"""
	
	cran = "syllabifyr" 

	version("0.1.1", md5="ddf9874852296cdb4a7a03606f982c0b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
