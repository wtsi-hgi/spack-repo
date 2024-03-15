# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadtextgrid(RPackage):
	"""Read in a 'Praat' 'TextGrid' File

	'Praat' <https://www.fon.hum.uva.nl/praat/> is a widely 
    used tool for manipulating, annotating and analyzing speech and 
    acoustic data. It stores annotation data in a format called a 
    'TextGrid'. This package provides a way to read these 
    files into R.
	"""
	
	homepage = "https://github.com/tjmahr/readtextgrid"
	cran = "readtextgrid" 

	version("0.1.2", md5="7840f874a4a1cda1c70b84aea290cf45")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
