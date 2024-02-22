# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhenery(RPackage):
	"""Modeling of Ordinal Random Variables via Softmax Regression

	Supports the modeling of ordinal random variables, 
    like the outcomes of races, via Softmax regression,
    under the Harville <doi:10.1080/01621459.1973.10482425> and
    Henery <doi:10.1111/j.2517-6161.1981.tb01153.x> models.
	"""
	
	homepage = "https://github.com/shabbychef/ohenery"
	cran = "ohenery" 

	version("0.1.1", md5="819f56a54786bfbd6bee3156950db534")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
