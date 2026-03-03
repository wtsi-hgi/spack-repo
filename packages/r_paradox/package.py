# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParadox(RPackage):
	"""Define and Work with Parameter Spaces for Complex Algorithms

	Define parameter spaces, constraints and
    dependencies for arbitrary algorithms, to program on such spaces. Also
    includes statistical designs and random samplers. Objects are
    implemented as 'R6' classes.
	"""
	
	homepage = "https://paradox.mlr-org.com"
	cran = "paradox" 

	version("0.11.1", md5="7e20bdd02fe901b6072991e6da7ded82")

	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3misc@0.9.4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
