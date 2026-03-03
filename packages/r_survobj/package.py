# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvobj(RPackage):
	"""Objects to Simulate Survival Times

	Generate objects that simulate survival times. Random values for the distributions are generated using the method described by Bender (2003) <https://epub.ub.uni-muenchen.de/id/eprint/1716> and Leemis (1987) in Operations Research, 35(6), 892–894.
	"""
	
	homepage = "https://johnaponte.github.io/survobj/"
	cran = "survobj" 

	version("3.0.0", md5="483850c5aa797d7136c0e4ad65f6a4f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
