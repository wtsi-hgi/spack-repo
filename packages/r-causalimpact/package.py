# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalimpact(RPackage):
	"""Inferring Causal Effects using Bayesian Structural Time-Series
Models

	Implements a Bayesian approach to causal impact estimation in time
  series, as described in Brodersen et al. (2015) <DOI:10.1214/14-AOAS788>.
  See the package documentation on GitHub
  <https://google.github.io/CausalImpact/> to get started.
	"""
	
	homepage = "https://google.github.io/CausalImpact/"
	cran = "CausalImpact" 

	version("1.3.0", md5="aae0ad99b2c708e1551e00be6ae27c76")

	depends_on("r-bsts@0.9:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-boom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
