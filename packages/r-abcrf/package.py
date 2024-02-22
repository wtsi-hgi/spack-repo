# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcrf(RPackage):
	"""Approximate Bayesian Computation via Random Forests

	Performs Approximate Bayesian Computation (ABC) model choice and parameter inference via random forests.
  Pudlo P., Marin J.-M., Estoup A., Cornuet J.-M., Gautier M. and Robert C. P. (2016) <doi:10.1093/bioinformatics/btv684>.
  Estoup A., Raynal L., Verdu P. and Marin J.-M. <http://journal-sfds.fr/article/view/709>.
  Raynal L., Marin J.-M., Pudlo P., Ribatet M., Robert C. P. and Estoup A. (2019) <doi:10.1093/bioinformatics/bty867>.
	"""
	
	cran = "abcrf" 

	version("1.9", md5="506f4cc36ae9d66bd174f4b65f8c3bb2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
