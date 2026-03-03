# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemtree(RPackage):
	"""Recursive Partitioning for Structural Equation Models

	SEM Trees and SEM Forests -- an extension of model-based decision
    trees and forests to Structural Equation Models (SEM). SEM trees hierarchically
    split empirical data into homogeneous groups each sharing similar data patterns
    with respect to a SEM by recursively selecting optimal predictors of these
    differences. SEM forests are an extension of SEM trees. They are ensembles of
    SEM trees each built on a random sample of the original data. By aggregating
    over a forest, we obtain measures of variable importance that are more robust
    than measures from single trees. A description of the method was published by
    Brandmaier, von Oertzen, McArdle, & Lindenberger (2013) <doi:10.1037/a0030001> 
    and Arnold, Voelkle, & Brandmaier (2020) <doi:10.3389/fpsyg.2020.564403>.
	"""
	
	homepage = "https://github.com/brandmaier/semtree"
	cran = "semtree" 

	version("0.9.19", md5="7f30ce597da09250ca9d952f3fd4e923")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-openmx@2.6.9:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot@3.0.6:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ctsemomx", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
