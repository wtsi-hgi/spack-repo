# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLitriddle(RPackage):
	"""Dataset and Tools to Research the Riddle of Literary Quality

	Dataset and functions to explore quality of literary novels. The package is a part of the Riddle of Literary Quality project, and it contains the data of a reader survey about fiction in Dutch, a description of the novels the readers rated, and the results of stylistic measurements of the novels. The package also contains functions to combine, analyze, and visualize these data. For more details, see: Eder M, van Zundert J, Lensink S, van Dalen-Oskam K (2022). Replicating The Riddle of Literary Quality: The litRiddle package for R. In _Digital Humanities 2022: Conference Abstracts_, 636-637.
	"""
	
	homepage = "https://literaryquality.huygens.knaw.nl/"
	cran = "litRiddle" 

	version("1.0.0", md5="a049e9975f09bf7abfa5f1a2c37ac0db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
