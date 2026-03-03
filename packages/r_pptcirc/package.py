# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPptcirc(RPackage):
	"""Projected Polya Tree for Circular Data

	Provides functionality for the prior and posterior projected Polya tree for the analysis of circular data 
  (Nieto-Barajas and Nunez-Antonio (2019) <arXiv:1902.06020>).
	"""
	
	homepage = "https://github.com/Karlampm/PPTcirc"
	cran = "PPTcirc" 

	version("0.2.3", md5="87308ec07029a24cf3336abd9ee2c14a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
