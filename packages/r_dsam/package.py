# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsam(RPackage):
	"""Data Splitting Algorithms for Model Developments

	Providing six different algorithms that can be used to split the 
    available data into training, test and validation subsets with similar distribution 
    for hydrological model developments. The dataSplit() function will help you divide 
    the data according to specific requirements, and you can refer to the par.default() 
    function to set the parameters for data splitting. The getAUC() function will help 
    you measure the similarity of distribution features between the data subsets.
    For more information about the data splitting algorithms, please refer to:
    Chen et al. (2022) <doi:10.1016/j.jhydrol.2022.128340>, 
    Zheng et al. (2022) <doi:10.1029/2021WR031818>.
	"""
	
	homepage = "https://github.com/lark-max/DSAM"
	cran = "DSAM" 

	version("1.0.2", md5="82ae0e618eddad6d2e747472b1f6b904")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
