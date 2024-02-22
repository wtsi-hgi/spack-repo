# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupclust(RPackage):
	"""Supervised Clustering of Predictor Variables Such as Genes

	Methodology for supervised grouping aka "clustering" of
   potentially many predictor variables, such as genes etc, implementing
   algorithms 'PELORA' and 'WILMA'.
	"""
	
	homepage = "https://github.com/mmaechler/supclust"
	cran = "supclust" 

	version("1.1-1", md5="4fe67c8499e6e7d4a37e48fbbe6a99b2")

	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
