# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmcm(RPackage):
	"""Modified Maximum Contrast Method

	An implementation of modified maximum contrast methods (Sato et al. (2009) <doi:10.1038/tpj.2008.17>;
  Nagashima et al. (2011) <doi:10.2202/1544-6115.1560>) and the maximum contrast method (Yoshimura et al. (1997)
  <doi:10.1177/009286159703100213>): Functions mmcm.mvt() and mcm.mvt() give P-value by using randomized quasi-Monte
  Carlo method with pmvt() function of package 'mvtnorm', and mmcm.resamp() gives P-value by using a permutation method.
	"""
	
	cran = "mmcm" 

	version("1.2-8", md5="508b4cb5c36e53cb8a8b4c8fbd1847b4")

	depends_on("r-mvtnorm", type=("build", "run"))
