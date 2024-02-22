# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimg(RPackage):
	"""General-Purpose Gradient-Based Optimization

	Provides general purpose tools for helping users to implement steepest
             gradient descent methods for function optimization; for details see
             Ruder (2016) <arXiv:1609.04747v2>. Currently, the Steepest 2-Groups
             Gradient Descent and the Adaptive Moment Estimation (Adam) are the
             methods implemented. Other methods will be implemented in the future.
	"""
	
	homepage = "https://github.com/vthorrf/optimg"
	cran = "optimg" 

	version("0.1.2", md5="9c487e54d113627abbcef66560b020f5")

	depends_on("r-ucminf@1.1.4:", type=("build", "run"))
