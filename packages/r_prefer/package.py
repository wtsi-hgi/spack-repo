# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrefer(RPackage):
	"""R Package for Pairwise Preference Elicitation

	Allows users to derive multi-objective weights from pairwise comparisons, which
    research shows is more repeatable, transparent, and intuitive other techniques. These weights
    can be rank existing alternatives or to define a multi-objective utility function for optimization.
	"""
	
	homepage = "https://github.com/jlepird/prefeR"
	cran = "prefeR" 

	version("0.1.3", md5="ae77fe122014eb42b8d742f1a00cf3aa")

	depends_on("r-mcmc", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
