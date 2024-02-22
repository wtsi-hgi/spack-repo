# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixmeta(RPackage):
	"""An Extended Mixed-Effects Framework for Meta-Analysis

	A collection of functions to perform various meta-analytical models
  through a unified mixed-effects framework, including standard univariate
  fixed and random-effects meta-analysis and meta-regression, and non-standard
  extensions such as multivariate, multilevel, longitudinal, and dose-response
  models.
	"""
	
	homepage = "https://github.com/gasparrini/mixmeta"
	cran = "mixmeta" 

	version("1.2.0", md5="092c6386a04fe29a6676d28b47c8fc3f")

	depends_on("r@3.5:", type=("build", "run"))
