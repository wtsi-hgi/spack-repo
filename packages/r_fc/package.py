# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFc(RPackage):
	"""Standard Evaluation-Based Multivariate Function Composition

	Provides a streamlined, standard evaluation-based approach to multivariate function composition. Allows for chaining commands via a forward-pipe operator, %>%.
	"""
	
	homepage = "https://github.com/swang87/fc"
	cran = "fc" 

	version("0.1.0", md5="925ae4e7b89252570058f4607fcdb86a")

	depends_on("r-codetools", type=("build", "run"))
