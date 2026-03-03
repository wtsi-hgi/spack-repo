# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAggtrees(RPackage):
	"""Aggregation Trees

	Nonparametric data-driven approach to discovering heterogeneous subgroups in a selection-on-observables framework. 
    aggTrees allows researchers to assess whether there exists relevant heterogeneity in treatment effects by generating a sequence of optimal groupings, 
    one for each level of granularity. For each grouping, we obtain point estimation and inference about the Group Average Treatment Effects. 
    Please reference the use as Di Francesco (2022) <doi:10.2139/ssrn.4304256>.
	"""
	
	homepage = "https://riccardo-df.github.io/aggTrees/"
	cran = "aggTrees" 

	version("2.0.2", md5="3ed43dd1d658d2c7777074210b9c3807")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
