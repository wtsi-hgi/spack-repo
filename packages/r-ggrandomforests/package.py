# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgrandomforests(RPackage):
	"""Visually Exploring Random Forests

	Graphic elements for exploring Random Forests using the 'randomForest' or
    'randomForestSRC' package for survival, regression and classification forests and
    'ggplot2' package plotting.
	"""
	
	homepage = "https://github.com/ehrlinger/ggRandomForests"
	cran = "ggRandomForests" 

	version("2.2.1", md5="c0f46746669418e8480189467b92b90b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomforestsrc@1.5.5:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
