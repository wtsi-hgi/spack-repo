# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSysid(RPackage):
	"""System Identification in R

	Provides functions for constructing mathematical models of dynamical systems from measured input-output data. 
	"""
	
	cran = "sysid" 

	version("1.0.4", md5="4fa79769347af54e9fd5ba0d8e909921")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tframe", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
