# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExperiment(RPackage):
	"""R Package for Designing and Analyzing Randomized Experiments

	Provides various statistical methods for
  designing and analyzing randomized experiments. One functionality
  of the package is the implementation of randomized-block and
  matched-pair designs based on possibly multivariate pre-treatment
  covariates. The package also provides the tools to analyze various
  randomized experiments including cluster randomized experiments,
  two-stage randomized experiments, randomized experiments with 
  noncompliance, and randomized experiments with missing data.
	"""
	
	homepage = "https://github.com/kosukeimai/experiment"
	cran = "experiment" 

	version("1.2.1", md5="bb9e30f160eca33216bf55da6bf40b7b")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r@2.4:", type=("build", "run"))
