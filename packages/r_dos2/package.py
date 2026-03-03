# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDos2(RPackage):
	"""Design of Observational Studies, Companion to the Second Edition

	Contains data sets, examples and software from the Second Edition of "Design of Observational Studies"; see Rosenbaum, P.R. (2010)  <doi:10.1007/978-1-4419-1213-8>.
	"""
	
	cran = "DOS2" 

	version("0.5.2", md5="55d72cad017fed6824d1ae648aaf0747", url="https://cran.r-project.org/src/contrib/DOS2_0.5.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sensitivity2x2xk", type=("build", "run"))
	depends_on("r-sensitivitymult", type=("build", "run"))
	depends_on("r-sensitivitymv", type=("build", "run"))
	depends_on("r-senstrat", type=("build", "run"))
