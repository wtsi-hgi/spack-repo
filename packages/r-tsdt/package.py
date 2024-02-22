# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdt(RPackage):
	"""Treatment-Specific Subgroup Detection Tool

	Implements a method for identifying subgroups with superior response relative to the overall sample.
	"""
	
	homepage = "https://github.com/EliLillyCo/CRAN_TSDT"
	cran = "TSDT" 

	version("1.0.7", md5="2d3a6da7439dac41a6ed7a2cc006237e")

	depends_on("r-mlbench", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-party", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survrm2", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
