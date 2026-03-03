# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRusk(RPackage):
	"""Beautiful Graphical Representation of Multiplication Tables on a
Modular Circle

	By placing on a circle 10 points numbered from 1 to 10, and connecting them by a straight line to the point corresponding to its multiplication by 2. (1 must be connected to 1 * 2 = 2, point 2 must be set to 2 * 2 = 4, point 3 to 3 * 2 = 6 and so on). You will obtain an amazing geometric figure that complicates and beautifies itself by varying the number of points and the multiplication table you use.
	"""
	
	homepage = "https://github.com/ThinkR-open/rusk"
	cran = "rusk" 

	version("0.1.1", md5="89105b858e7e370e7cc58a8389336796")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
