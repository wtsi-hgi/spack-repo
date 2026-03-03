# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGretaDynamics(RPackage):
	"""Modelling Structured Dynamical Systems in 'greta'

	A 'greta' extension for analysing transition matrices and 
  ordinary differential equations representing dynamical systems. Provides 
  functions for analysing transition matrices by iteration, and solving 
  ordinary differential equations. This is an extension to the 'greta' 
  software, Golding (2019) <doi:10.21105/joss.01601>.
	"""
	
	homepage = "https://github.com/greta-dev/greta.dynamics"
	cran = "greta.dynamics" 

	version("0.2.0", md5="b33e8c905f3c37501fc6ea29df3ef50e")

	depends_on("r-greta@0.4.2:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tensorflow@1.14:", type=("build", "run"))
	depends_on("python@2.7.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow@1.14:", type=("build", "link", "run"))
	depends_on("py-tensorflow-probability", type=("build", "link", "run"))
