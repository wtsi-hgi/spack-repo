# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossdes(RPackage):
	"""Construction of Crossover Designs

	Contains functions for the construction of carryover
        balanced crossover designs. In addition contains functions to
        check given designs for balance.
	"""
	
	cran = "crossdes" 

	version("1.1-2", md5="68df5d766dbbfe9a5fe4ea307304c29a")

	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
