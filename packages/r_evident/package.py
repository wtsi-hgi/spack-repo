# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvident(RPackage):
	"""Evidence Factors in Observational Studies

	Contains a collection of examples of evidence factors in observational studies from the book Replication and Evidence Factors in Observational Studies by Paul R. Rosenbaum (2021) <doi:10.1201/9781003039648>.
	"""
	
	cran = "evident" 

	version("1.0.4", md5="eb4f64f5389263dcf2c4aefb5c99d1f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sensitivity2x2xk", type=("build", "run"))
	depends_on("r-sensitivitymult", type=("build", "run"))
	depends_on("r-sensitivitymv", type=("build", "run"))
	depends_on("r-senstrat", type=("build", "run"))
	depends_on("r-dos2", type=("build", "run"))
