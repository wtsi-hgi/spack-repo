# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenix(RPackage):
	"""Phenotypic Integration Index

	Provides functions to estimate the size-controlled phenotypic integration index, a novel method by Torices & Méndez (2014) to solve problems due to individual size when estimating integration (namely, larger individuals have larger components, which will drive a correlation between components only due to resource availability that might obscure the observed measures of integration). In addition, the package also provides the classical estimation by Wagner (1984), bootstrapping and jackknife methods to calculate confidence intervals and a significance test for both integration indices.
	"""
	
	cran = "PHENIX" 

	version("1.3.1", md5="b660d91802430769dd9c586ad519fa2c")

	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
