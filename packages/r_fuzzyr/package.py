# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyr(RPackage):
	"""Fuzzy Logic Toolkit for R

	Design and simulate fuzzy logic systems using Type-1 and Interval Type-2 Fuzzy Logic.
    This toolkit includes with graphical user interface (GUI) and an adaptive neuro-
    fuzzy inference system (ANFIS). This toolkit is a continuation from the previous
    package ('FuzzyToolkitUoN'). Produced by the Intelligent Modelling & Analysis Group (IMA)
    and Lab for UnCertainty In Data and decision making (LUCID), University of Nottingham. 
    A big thank you to the many people who have contributed to the development/evaluation of the toolbox.
    Please cite the toolbox and the corresponding paper <doi:10.1109/FUZZ48607.2020.9177780> when using it.
    More related papers can be found in the NEWS.
	"""
	
	homepage = "https://www.lucidresearch.org/"
	cran = "FuzzyR" 

	version("2.3.2", md5="ed7572720cb9687879a84c6d45965297")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
