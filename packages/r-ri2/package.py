# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRi2(RPackage):
	"""Randomization Inference for Randomized Experiments

	Randomization inference procedures for simple and complex randomized designs, including multi-armed trials, as described in Gerber and Green (2012, ISBN: 978-0393979954). Users formally describe their randomization procedure and test statistic. The randomization distribution of the test statistic under some null hypothesis is efficiently simulated.
	"""
	
	cran = "ri2" 

	version("0.4.0", md5="b65de6a7a8c3e9becef4d0b67bd3f711", url="https://cran.r-project.org/src/contrib/ri2_0.4.0.tar.gz")

	depends_on("r-randomizr@0.16:", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
