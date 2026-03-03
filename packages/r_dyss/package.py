# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyss(RPackage):
	"""Dynamic Screening Systems

	In practice, we will encounter problems where the longitudinal performance of processes needs to be monitored over time. 
  Dynamic screening systems (DySS) are methods that aim to identify and give signals to processes with poor performance as early as possible. 
  This package is designed to implement dynamic screening systems and the related methods.
  References:
  Qiu, P. and Xiang, D. (2014) <doi:10.1080/00401706.2013.822423>;
  Qiu, P. and Xiang, D. (2015) <doi:10.1002/sim.6477>;
  Li, J. and Qiu, P. (2016) <doi:10.1080/0740817X.2016.1146423>;
  Li, J. and Qiu, P. (2017) <doi:10.1002/qre.2160>;
  You, L. and Qiu, P. (2019) <doi:10.1080/00949655.2018.1552273>;
  Qiu, P., Xia, Z., and You, L. (2020) <doi:10.1080/00401706.2019.1604434>;
  You, L., Qiu, A., Huang, B., and Qiu, P. (2020) <doi:10.1002/bimj.201900127>;
  You, L. and Qiu, P. (2021) <doi:10.1080/00224065.2020.1767006>.
	"""
	
	cran = "DySS" 

	version("1.0", md5="ebffbb97e62c749fbe78704468ebbdbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
