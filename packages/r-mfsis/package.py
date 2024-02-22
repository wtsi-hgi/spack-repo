# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfsis(RPackage):
	"""Moder-Free Sure Independent Screening Procedures

	An implementation of popular screening methods that are commonly 
  employed in ultra-high and high dimensional data. Through this publicly 
  available package, we provide a unified framework to carry out model-free 
  screening procedures including 
  SIS (Fan and Lv (2008) <doi:10.1111/j.1467-9868.2008.00674.x>), 
  SIRS(Zhu et al. (2011)<doi:10.1198/jasa.2011.tm10563>), 
  DC-SIS (Li et al. (2012) <doi:10.1080/01621459.2012.695654>), 
  MDC-SIS(Shao and Zhang (2014) <doi:10.1080/01621459.2014.887012>), 
  Bcor-SIS (Pan et al. (2019) <doi:10.1080/01621459.2018.1462709>), 
  PC-Screen (Liu et al. (2020) <doi:10.1080/01621459.2020.1783274>), 
  WLS (Zhong et al.(2021) <doi:10.1080/01621459.2021.1918554>), 
  Kfilter (Mai and Zou (2015) <doi:10.1214/14-AOS1303>), 
  MVSIS (Cui et al. (2015) <doi:10.1080/01621459.2014.920256>), 
  PSIS (Pan et al. (2016) <doi:10.1080/01621459.2014.998760>), 
  CAS (Xie et al. (2020) <doi:10.1080/01621459.2019.1573734>), 
  CI-SIS (Cheng and Wang. (2022) <doi:10.1016/j.cmpb.2022.107269>)and CSIS.
	"""
	
	cran = "MFSIS" 

	version("0.2.0", md5="dbe89ba97ec17a052cc35d97632af604")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ball", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("python@3.8.0:", type=("build", "link", "run"))
