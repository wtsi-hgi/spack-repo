# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignmatch(RPackage):
	"""Matched Samples that are Balanced and Representative by Design

	Includes functions for the construction of matched samples that are balanced and representative by design.  Among others, these functions can be used for matching in observational studies with treated and control units, with cases and controls, in related settings with instrumental variables, and in discontinuity designs.  Also, they can be used for the design of randomized experiments, for example, for matching before randomization.  By default, 'designmatch' uses the 'highs' optimization solver, but its performance is greatly enhanced by the 'Gurobi' optimization solver and its associated R interface.  For their installation, please follow the instructions at <https://www.gurobi.com/documentation/quickstart.html> and <https://www.gurobi.com/documentation/7.0/refman/r_api_overview.html>.  We have also included directions in the gurobi_installation file in the inst folder.
	"""
	
	cran = "designmatch" 

	version("0.5.4", md5="35c178881dbd5c42119d23d090130a70")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-highs", type=("build", "run"))
