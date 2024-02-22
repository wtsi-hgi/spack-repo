# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlan(RPackage):
	"""FLuctuation ANalysis on Mutation Models

	Tools for fluctuations analysis of mutant cells counts. Main reference is A. Mazoyer, R. Drouilhet, S. Despreaux and B. Ycart (2017)  <doi:10.32614/RJ-2017-029>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "flan" 

	version("0.9", md5="9beda2887dbe29b08bb94fe203533f1f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
