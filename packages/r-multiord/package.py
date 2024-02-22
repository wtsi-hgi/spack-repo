# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiord(RPackage):
	"""Generation of Multivariate Ordinal Variates

	A method for multivariate ordinal data generation given marginal distributions and correlation matrix based on the methodology proposed by Demirtas (2006) <DOI:10.1080/10629360600569246>.
	"""
	
	cran = "MultiOrd" 

	version("2.4.3", md5="bd56d20299455f3f56d140303ca6ab7c")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
