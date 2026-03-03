# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgritutorial(RPackage):
	"""Tutorial Analysis of Some Agricultural Experiments

	Example software for the analysis of data from designed 
	experiments, especially agricultural crop experiments. The basics 
	of the analysis of designed experiments are discussed 
	using real examples from agricultural field trials. 
	A range of statistical methods using a range
	of R statistical packages are  exemplified . The experimental
	data is made available as separate data sets for each example
	and the R analysis code is made available as example code.
	The example code can be readily extended, as required.
	"""
	
	cran = "agriTutorial" 

	version("0.1.5", md5="d5be2ac52bea5eb0b9bcdde417466b69")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
