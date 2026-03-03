# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticlasspairs(RPackage):
	"""Build MultiClass Pair-Based Classifiers using TSPs or RF

	A toolbox to train a single sample classifier that uses in-sample feature relationships. The relationships are represented as feature1 < feature2 (e.g. gene1 < gene2). We provide two options to go with. First is based on 'switchBox' package which uses Top-score pairs algorithm. Second is a novel implementation based on random forest algorithm. For simple problems we recommend to use one-vs-rest using TSP option due to its simplicity and for being easy to interpret.  For complex problems RF performs better.  Both lines filter the features first then combine the filtered features to make the list of all the possible rules (i.e. rule1: feature1 < feature2, rule2: feature1 < feature3, etc...).  Then the list of rules will be filtered and the most important and informative rules will be kept. The informative rules will be assembled in an one-vs-rest model or in an RF model.  We provide a detailed description with each function in this package to explain the filtration and training methodology in each line. Reference: Marzouka & Eriksson (2021) <doi:10.1093/bioinformatics/btab088>.
	"""
	
	homepage = "https://github.com/NourMarzouka/multiclassPairs"
	cran = "multiclassPairs" 

	version("0.4.3", md5="60f9e6f0c39a4cf2ebdf1f400eda4eb9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-boruta", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
