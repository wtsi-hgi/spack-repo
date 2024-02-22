# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirtualpollen(RPackage):
	"""Simulating Pollen Curves from Virtual Taxa with Different Life
and Niche Traits

	Tools to generate virtual environmental drivers with a given temporal autocorrelation, and to simulate pollen curves at annual resolution over millennial time-scales based on these drivers and virtual taxa with different life traits and niche features. It also provides the means to simulate quasi-realistic pollen-data conditions by applying simulated accumulation rates and given depth intervals between consecutive samples.
	"""
	
	homepage = "https://github.com/BlasBenito/virtualPollen"
	cran = "virtualPollen" 

	version("1.0.1", md5="815276bf5df58e72ce7198839b8db7af")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
