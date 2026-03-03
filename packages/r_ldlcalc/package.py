# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdlcalc(RPackage):
	"""Calculate and Predict the Low Density Lipoprotein Values

	A wide variety of ways to calculate (through equations) or predict (using 9 Machine learning methods as well as a stack algorithm combination of them all) the Low Density Lipoprotein values of patients based on the values of three other metrics, namely Total Cholesterol , Triglycerides and High Density Lipoprotein. It can also calculate the variance of LDL and the Atherogenic Index of Plasma (AIP) using error propagation and bootstrapping.
	"""
	
	cran = "LDLcalc" 

	version("2.1", md5="6f106c28bb5aa93e1abc1392c65636ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-caretensemble", type=("build", "run"))
	depends_on("r-lares", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-resample", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
