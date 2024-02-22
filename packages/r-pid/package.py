# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPid(RPackage):
	"""Process Improvement using Data

	A collection of scripts and data files for the statistics text: 
 "Process Improvement using Data" <https://learnche.org/pid> and the online 
 course "Experimentation for Improvement" found on Coursera. The package 
 contains code for designed experiments, data sets and other convenience 
 functions used in the book.
	"""
	
	homepage = "https://learnche.org/pid"
	cran = "pid" 

	version("0.50", md5="e3938cc55fe3d4aa0b46ed2a5cfac0f7")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-frf2", type=("build", "run"))
	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-frf2-catlg128", type=("build", "run"))
