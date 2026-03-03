# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquatemultiple(RPackage):
	"""Equating of Multiple Forms

	Equating of multiple forms using Item Response Theory (IRT) methods (Battauz M. (2017) <doi:10.1007/s11336-016-9517-x> and Haberman S. J. (2009) <doi:10.1002/j.2333-8504.2009.tb02197.x>).
	"""
	
	cran = "equateMultiple" 

	version("0.1.2", md5="d1f6787c4020f80c97f66fe7cb8162df")

	depends_on("r-equateirt@2.0.4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
