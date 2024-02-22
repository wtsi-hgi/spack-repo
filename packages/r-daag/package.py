# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaag(RPackage):
	"""Data Analysis and Graphics Data and Functions

	Functions and data sets used in examples and exercises in the
        text Maindonald, J.H. and Braun, W.J. (2003, 2007, 2010) "Data
        Analysis and Graphics Using R", and in an upcoming Maindonald,
        Braun, Andrews, and Narayan text that builds on this earlier text.
	"""
	
	homepage = "https://gitlab.com/daagur"
	cran = "DAAG" 

	version("1.25.4", md5="0444d36aca776e5137b5de8022692c0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
