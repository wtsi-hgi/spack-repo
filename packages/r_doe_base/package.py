# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoeBase(RPackage):
	"""Full Factorials, Orthogonal Arrays and Base Utilities for DoE
Packages

	Creates full factorial experimental designs and designs based on orthogonal arrays for (industrial) experiments. Provides diverse quality criteria. Provides utility functions for the class design, which is also used by other packages for designed experiments.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/DoE/"
	cran = "DoE.base" 

	version("1.2-4", md5="1ae4025e44d542e3c639a43a191a5318")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-conf-design", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
