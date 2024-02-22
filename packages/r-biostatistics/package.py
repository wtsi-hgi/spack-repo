# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiostatistics(RPackage):
	"""Statistics Tutorials for Biologists

	Tutorials for statistics, aimed at biological scientists. 
    Subjects range from basic descriptive statistics 
    through to complex linear modelling. The tutorials
    include text, videos, interactive coding exercises
    and multiple choice quizzes. The package also 
    includes 19 datasets which are used in the 
    tutorials.
	"""
	
	cran = "Biostatistics" 

	version("1.0.4", md5="7ecebec885210df154c3b6eb740678a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-learnr", type=("build", "run"))
