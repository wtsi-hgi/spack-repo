# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrreg(RPackage):
	"""MDL Multiresolution Linear Regression Framework

	We provide the framework to analyze multiresolution partitions (e.g. country, provinces, subdistrict) where each individual data point belongs to only one partition in each layer (e.g. i belongs to subdistrict A, province P, and country Q).   We assume that a partition in a higher layer subsumes lower-layer partitions (e.g. a nation is at the 1st layer subsumes all provinces at the 2nd layer). Given N individuals that have a pair of real values (x,y) that generated from  independent variable X and dependent variable Y. Each individual i belongs to one partition per layer. Our goal is to find which partitions at which highest level that all individuals  in the these partitions share the same linear model Y=f(X) where f is a linear function. The framework deploys the Minimum Description Length principle (MDL) to infer solutions. The publication of this package is at Chainarong Amornbunchornvej, Navaporn Surasvadi, Anon Plangprasopchok, and Suttipong Thajchayapong (2021) <doi:10.1145/3424670>.
	"""
	
	homepage = "https://github.com/DarkEyes/MRReg"
	cran = "MRReg" 

	version("0.1.5", md5="cf268a756bf406ad423987eb948ea68b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
