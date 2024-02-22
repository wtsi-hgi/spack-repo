# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquivalence(RPackage):
	"""Provides Tests and Graphics for Assessing Tests of Equivalence

	Provides statistical tests and graphics for assessing tests
        of equivalence.  Such tests have similarity as the alternative
	hypothesis instead of the null.  Sample data sets are included.
	"""
	
	cran = "equivalence" 

	version("0.7.2", md5="0b960e89b44debe4e8985572fcfb98cf")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-paireddata", type=("build", "run"))
