# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRorqualMorpho(RPackage):
	"""Morphological Allometry of Rorquals

	Predicts morphological parameters of rorquals (e.g. body mass, 
    flipper length, maximum engulfment capacity) from body length using 
    allometric equations from Kahane-Rapport and Goldbogen (2018) 
    <doi:10.1002/jmor.20846>.
	"""
	
	cran = "rorqual.morpho" 

	version("0.1.1", md5="b42a79024a2ec984c6811d86b060a60f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
