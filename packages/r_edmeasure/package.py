# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdmeasure(RPackage):
	"""Energy-Based Dependence Measures

	Implementations of (1) mutual dependence measures and mutual independence tests in 
    Jin, Z., and Matteson, D. S. (2017) <arXiv:1709.02532>;
    (2) independent component analysis methods based on mutual dependence measures in 
    Jin, Z., and Matteson, D. S. (2017) <arXiv:1709.02532> 
    and Pfister, N., et al. (2018) <doi:10.1111/rssb.12235>;
    (3) conditional mean dependence measures and conditional mean independence tests in 
    Shao, X., and Zhang, J. (2014) <doi:10.1080/01621459.2014.887012>,
    Park, T., et al. (2015) <doi:10.1214/15-EJS1047>,
    and Lee, C. E., and Shao, X. (2017) <doi:10.1080/01621459.2016.1240083>.
	"""
	
	cran = "EDMeasure" 

	version("1.2.0", md5="0df2d434dceb7afcf2b9ffe6d8b1b756")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-energy@1.7.0:", type=("build", "run"))
	depends_on("r-dhsic@2:", type=("build", "run"))
	depends_on("r-rbayesianoptimization@1.1:", type=("build", "run"))
