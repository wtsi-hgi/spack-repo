# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsga3(RPackage):
	"""An Implementation of Non-Dominated Sorting Genetic Algorithm III
for Feature Selection

	An adaptation of Non-dominated Sorting Genetic Algorithm III for multi objective 
    feature selection tasks. Non-dominated Sorting Genetic Algorithm III is a genetic algorithm
    that solves multiple optimization problems simultaneously by applying a non-dominated sorting 
    technique. It uses a reference points based selection operator to explore 
    solution space and preserve diversity. See the original paper by K. Deb and 
    H. Jain (2014) <DOI:10.1109/TEVC.2013.2281534> for a detailed description.
	"""
	
	cran = "nsga3" 

	version("0.0.3", md5="7501a16fed4a0f833fda4ff8b513a72d", url="https://cran.r-project.org/src/contrib/nsga3_0.0.3.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
	depends_on("r-parallelmap", type=("build", "run"))
	depends_on("r-rpref", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
