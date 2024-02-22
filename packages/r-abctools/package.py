# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbctools(RPackage):
	"""Tools for ABC Analyses

	Tools for approximate Bayesian computation including summary statistic selection and assessing coverage.
    See Nunes and Prangle (2015) <doi:10.32614/RJ-2015-030> and Rodrigues, Prangle and Sisson (2018) <doi:10.1016/j.csda.2018.04.004>.
	"""
	
	homepage = "https://github.com/dennisprangle/abctools"
	cran = "abctools" 

	version("1.1.7", md5="1715682182f3aa3800f77e6525989a19")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abc", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
