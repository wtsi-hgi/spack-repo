# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlacco(RPackage):
	"""Feature-Based Landscape Analysis of Continuous and Constrained
Optimization Problems

	Tools and features for "Exploratory Landscape Analysis (ELA)" of
	single-objective continuous optimization problems.
    Those features are able to quantify rather complex properties, such as the
    global structure, separability, etc., of the optimization problems.
	"""
	
	homepage = "https://github.com/kerschke/flacco"
	cran = "flacco" 

	version("1.8", md5="0ca7cfc6f53029224c17be11edefa9f7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mlr", type=("build", "run"))
