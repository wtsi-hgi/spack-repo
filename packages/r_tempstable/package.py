# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTempstable(RPackage):
	"""A Collection of Methods to Estimate Parameters of Different
Tempered Stable Distributions

	
  A collection of methods to estimate parameters of different tempered stable 
  distributions (TSD). Currently, there are seven different tempered stable 
  distributions to choose from: Tempered stable subordinator distribution, 
  classical TSD, generalized classical TSD, normal TSD, modified TSD, rapid 
  decreasing TSD, and Kim-Rachev TSD.
  The package also provides functions to compute density and probability 
  functions and tools to run Monte Carlo simulations.
  This package has already been used for the estimation of tempered stable 
  distributions (Massing (2023) <arXiv:2303.07060>).
  The following references form the theoretical background for various functions
  in this package. References for each function are explicitly listed in its 
  documentation:
  Bianchi et al. (2010) <doi:10.1007/978-88-470-1481-7_4>
  Bianchi et al. (2011) <doi:10.1137/S0040585X97984632>
  Carrasco (2017) <doi:10.1017/S0266466616000025>
  Feuerverger (1981) <doi:10.1111/j.2517-6161.1981.tb01143.x>
  Hansen et al. (1996) <doi:10.1080/07350015.1996.10524656>
  Hansen (1982) <doi:10.2307/1912775>
  Hofert (2011) <doi:10.1145/2043635.2043638>
  Kawai & Masuda (2011) <doi:10.1016/j.cam.2010.12.014>
  Kim et al. (2008) <doi:10.1016/j.jbankfin.2007.11.004>
  Kim et al. (2009) <doi:10.1007/978-3-7908-2050-8_5>
  Kim et al. (2010) <doi:10.1016/j.jbankfin.2010.01.015>
  Kuechler & Tappe (2013) <doi:10.1016/j.spa.2013.06.012>
  Rachev et al. (2011) <doi:10.1002/9781118268070>.
	"""
	
	homepage = "https://github.com/TMoek/TempStable"
	cran = "TempStable" 

	version("0.2.2", md5="808c1ddc47e46c55e01cc96f2a4527ae")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-copula@1.1.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.12:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-gsl@2.1.8:", type=("build", "run"))
	depends_on("r-hypergeo@1.2.13:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1:", type=("build", "run"))
	depends_on("r-stabledist@0.7.1:", type=("build", "run"))
	depends_on("r-stableestim@2.1:", type=("build", "run"))
	depends_on("r-rootsolve@1.8:", type=("build", "run"))
	depends_on("r-vgam@1.1.7:", type=("build", "run"))
