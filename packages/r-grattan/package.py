# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrattan(RPackage):
	"""Australian Tax Policy Analysis

	Utilities to cost and evaluate Australian tax policy, including fast
    projections of personal income tax collections, high-performance tax and 
    transfer calculators, and an interface to common indices from the Australian
    Bureau of Statistics.  Written to support Grattan Institute's Australian 
    Perspectives program, and related projects. Access to the Australian Taxation
    Office's sample files of personal income tax returns is assumed. 
	"""
	
	homepage = "https://github.com/HughParsonage/grattan"
	cran = "grattan" 

	version("2024.1.1", md5="106b4733e886b29524a5f8785454966d")
	version("2024.0.0", md5="575d7f1a8911d8cb8c0ccf49f81b34b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-grattaninflators@0.4:", type=("build", "run"))
	depends_on("r-hutils@1.3:", type=("build", "run"))
	depends_on("r-hutilscpp@0.9:", type=("build", "run"))
	depends_on("r-ineq@0.2.10:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-fy@0.2:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
