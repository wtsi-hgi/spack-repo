# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfilemodel(RPackage):
	"""Profiling Inference Functions for Various Model Classes

	Provides tools that can be used to calculate, evaluate, plot and use for inference the profiles of *arbitrary* inference functions for *arbitrary* 'glm'-like fitted models with linear predictors. More information on the methods that are implemented can be found in Kosmidis (2008) <https://www.r-project.org/doc/Rnews/Rnews_2008-2.pdf>.
	"""
	
	homepage = "https://github.com/ikosmidis/profileModel"
	cran = "profileModel" 

	version("0.6.1", md5="4e6b2c73ecfc85cc289c0612fa27c33e")

	depends_on("r@2.6:", type=("build", "run"))
