# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlse(RPackage):
	"""Linear Regression Based on 'ILSE' for Missing Data

	Linear regression when covariates include missing values by embedding the 
    correlation information between covariates. Especially for block missing data,
    it works well. 'ILSE' conducts imputation and regression simultaneously and iteratively. 
    More details can be referred to 
    Huazhen Lin, Wei Liu and Wei Lan. (2021) <doi:10.1080/07350015.2019.1635486>.
	"""
	
	homepage = "https://github.com/feiyoung/ILSE"
	cran = "ILSE" 

	version("1.1.7", md5="126d88e5f0a4514e7d2e79ed384bc762")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
