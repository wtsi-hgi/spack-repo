# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaswr(RPackage):
	"""Probability and Statistics with R

	Functions and data sets for the text Probability and Statistics
    with R.
	"""
	
	cran = "PASWR" 

	version("1.3", md5="54b94fa5fa9df48aaf652aac119f3a33")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
