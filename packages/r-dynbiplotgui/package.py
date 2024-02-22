# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynbiplotgui(RPackage):
	"""Full Interactive GUI for Dynamic Biplot in R

	A GUI to solve dynamic biplots and classical biplot. Try matrices
    of 2-way and 3-way. The GUI can be run in multiple languages.
	"""
	
	cran = "dynBiplotGUI" 

	version("1.1.6", md5="836a2f2e88219c4b1fc8e73691af9e6d")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-tcltk2@1.2.10:", type=("build", "run"))
	depends_on("gmake", type=("build", "link", "run"))
