# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlba(RPackage):
	"""General Linear Ballistic Accumulator Models

	Analyses response times and accuracies from psychological experiments with the linear ballistic accumulator (LBA) model from Brown and Heathcote (2008). The LBA model is optionally fitted with explanatory variables on the parameters such as the drift rate, the boundary and the starting point parameters. A log-link function on the linear predictors can be used to ensure that parameters remain positive when needed.  
	"""
	
	cran = "glba" 

	version("0.2.1", md5="5f3c13a7258193a5fd1eaf8fa0dbd9a1")

	depends_on("r@3.1.2:", type=("build", "run"))
