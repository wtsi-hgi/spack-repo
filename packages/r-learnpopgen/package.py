# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnpopgen(RPackage):
	"""Population Genetic Simulations & Numerical Analysis

	Conducts various numerical analyses and simulations in population genetics and evolutionary theory, primarily for the purpose of teaching (and learning about) key concepts in population & quantitative genetics, and evolutionary theory.
	"""
	
	homepage = "http://github.com/liamrevell/learnPopGen"
	cran = "learnPopGen" 

	version("1.0.4", md5="215a84def15923b76623e84ca78ecd37")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
