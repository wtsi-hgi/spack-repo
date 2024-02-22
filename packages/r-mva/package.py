# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMva(RPackage):
	"""An Introduction to Applied Multivariate Analysis with R

	Functions, data sets, analyses and examples from the book 
  `An Introduction to Applied Multivariate Analysis with R' 
  (Brian S. Everitt and Torsten Hothorn, Springer, 2011). 
	"""
	
	homepage = "http://dx.doi.org/10.1007/978-1-4419-9650-3"
	cran = "MVA" 

	version("1.0-8", md5="4e01272d4da66c81737eb4100cc31750")

	depends_on("r-hsaur2", type=("build", "run"))
