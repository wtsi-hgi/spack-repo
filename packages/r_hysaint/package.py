# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHysaint(RPackage):
	"""Hybrid Genetic and Simulated Annealing for Variable Selection

	We provide a stage-wise selection method using genetic algorithms, designed to efficiently identify main and two-way interactions within high-dimensional linear regression models. Additionally, it implements simulated annealing algorithms during the mutation process. The relevant paper can be found at: Ye, C.,and Yang,Y. (2019) <doi:10.1109/TIT.2019.2913417>.
	"""
	
	cran = "hySAINT" 

	version("1.2.0", md5="615537cf1c70d8ce0130f6deba1c1974")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-selectiveinference", type=("build", "run"))
	depends_on("r-variablescreening", type=("build", "run"))
	depends_on("r-sis", type=("build", "run"))
