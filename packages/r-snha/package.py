# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnha(RPackage):
	"""Creating Correlation Networks using St. Nicolas House Analysis

	
    Create correlation networks using St. Nicolas House Analysis ('SNHA'). 
    The package can be used for visualizing multivariate data similar to Principal
    Component Analysis or Multidimensional Scaling using a ranking approach.
    In contrast to 'MDS' and 'PCA', 'SNHA' uses a network approach to explore
    interacting variables. 
    For details see 'Hermanussen et. al. 2021', <doi:10.3390/ijerph18041741>.
	"""
	
	homepage = "https://github.com/mittelmark/snha"
	cran = "snha" 

	version("0.1.3", md5="4f520921a24f10f7a05fb00f6acc9713")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
