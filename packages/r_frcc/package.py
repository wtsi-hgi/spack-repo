# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrcc(RPackage):
	"""Fast Regularized Canonical Correlation Analysis

	Contains the core functions associated with Fast
        Regularized Canonical Correlation Analysis. Please see the following for
        details: Raul Cruz-Cano, Mei-Ling Ting Lee, 
        Fast regularized canonical correlation analysis, 
        Computational Statistics & Data Analysis, 
        Volume 70, 2014, Pages 88-100, 
        ISSN 0167-9473 <doi:10.1016/j.csda.2013.09.020>.
	"""
	
	cran = "FRCC" 

	version("1.1.0", md5="b1632d8c72bb60d7a5b4058f0715d762")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-calibrate", type=("build", "run"))
	depends_on("r-ccp", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
