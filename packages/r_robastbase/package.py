# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobastbase(RPackage):
	"""Robust Asymptotic Statistics

	Base S4-classes and functions for robust asymptotic statistics.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/robast/"
	cran = "RobAStBase" 

	version("1.2.5", md5="33e4ee7e56a0f67c33b1ae60030f5ca3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-distr@2.8:", type=("build", "run"))
	depends_on("r-distrex@2.8:", type=("build", "run"))
	depends_on("r-distrmod@2.8.1:", type=("build", "run"))
	depends_on("r-randvar@1.2:", type=("build", "run"))
	depends_on("r-startupmsg", type=("build", "run"))
