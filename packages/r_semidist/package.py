# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemidist(RPackage):
	"""Measure Dependence Between Categorical and Continuous Variables

	Semi-distance and mean-variance (MV) index are proposed to measure the dependence between a categorical random variable and a continuous variable.
    Test of independence and feature screening for classification problems can be implemented via the two dependence measures.
    For the details of the methods, see Zhong et al. (2023) <doi:10.1080/01621459.2023.2284988>;
    Cui and Zhong (2019) <doi:10.1016/j.csda.2019.05.004>;
    Cui, Li and Zhong (2015) <doi:10.1080/01621459.2014.920256>.
	"""
	
	homepage = "https://github.com/wzhong41/semidist"
	cran = "semidist" 

	version("0.1.0", md5="0bc127fe83196ffa9eb54e215be010c7")

	depends_on("r-energy", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
