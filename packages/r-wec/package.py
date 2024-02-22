# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWec(RPackage):
	"""Weighted Effect Coding

	Provides functions to create factor variables with contrasts based on weighted effect coding, and their interactions. In weighted effect coding the estimates from a first order regression model show the deviations per group from the sample mean. This is especially useful when a researcher has no directional hypotheses and uses a sample from a population in which the number of observation per group is different.
	"""
	
	homepage = "http://www.ru.nl/sociology/mt/wec/downloads/"
	cran = "wec" 

	version("0.4-1", md5="ad2c2fb8a5deec591a4fde34e669e14b")

	depends_on("r-dplyr", type=("build", "run"))
