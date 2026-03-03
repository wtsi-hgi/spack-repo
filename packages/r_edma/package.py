# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdma(RPackage):
	"""Dynamic Model Averaging with Grid Search

	Perform dynamic model averaging with grid search as in Dangl and Halling (2012) <doi:10.1016/j.jfineco.2012.04.003> using parallel computing.
	"""
	
	cran = "eDMA" 

	version("1.5-3", md5="d79afb575568fdb02d4f96194c7d9f4e")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
