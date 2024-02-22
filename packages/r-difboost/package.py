# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifboost(RPackage):
	"""Detection of Differential Item Functioning (DIF) in Rasch Models
by Boosting Techniques

	Performs detection of Differential Item Functioning using the method DIFboost as proposed by Schauberger and Tutz (2016) <doi:10.1111/bmsp.12060>. 
	"""
	
	cran = "DIFboost" 

	version("0.3", md5="9ba8bb3baf296b7431bce6dfc677eab2")

	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-stabs", type=("build", "run"))
