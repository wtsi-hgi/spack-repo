# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetrender(RPackage):
	"""A Graphical User Interface (GUI) to Visualize and Analyze
Dendrochronological Data

	A Graphical User Interface (GUI) to import, save, detrend and 
    perform standard tree-ring analyses. The interactive detrending allows the user to check how
    well the detrending curve fits each time-series and change it when needed.
	"""
	
	cran = "detrendeR" 

	version("1.0.5", md5="2326c5e83a393ffd201ac6ab29c2e7e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-tkrplotr", type=("build", "run"))
