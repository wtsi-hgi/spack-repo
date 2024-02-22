# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiflasso(RPackage):
	"""A Penalty Approach to Differential Item Functioning in Rasch
Models

	Performs DIFlasso as proposed by Tutz and Schauberger (2015) <doi:10.1007/s11336-013-9377-6>, a method to detect DIF (Differential Item Functioning) in Rasch Models. It can handle settings with many variables and also metric variables. 
	"""
	
	cran = "DIFlasso" 

	version("1.0-4", md5="2a942071f8665a0760b709ef70484393")

	depends_on("r-grplasso", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
