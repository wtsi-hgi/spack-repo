# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsindicators(RPackage):
	"""Climate Services' Indicators Based on Sub-Seasonal to Decadal
Predictions

	Set of generalised tools for the flexible computation of climate 
  related indicators defined by the user. Each method represents a specific 
  mathematical approach which is combined with the possibility to select an 
  arbitrary time period to define the indicator. This enables a wide range of 
  possibilities to tailor the most suitable indicator for each particular climate 
  service application (agriculture, food security, energy, water management, ...). 
  This package is intended for sub-seasonal, seasonal and decadal climate 
  predictions, but its methods are also applicable to other time-scales, 
  provided the dimensional structure of the input is maintained. Additionally, 
  the outputs of the functions in this package are compatible with 'CSTools'. 
  This package is described in 'Pérez-Zanón et al. (2023) 
  <doi:10.1016/j.cliser.2023.100393>' and it was developed in the context of 
  'H2020 MED-GOLD' (776467) and 'S2S4E' (776787) projects. See 'Lledó et al. (2019) 
  <doi:10.1016/j.renene.2019.04.135>' and 'Chou et al., 2023 
  <doi:10.1016/j.cliser.2023.100345>' for details.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/csindicators/"
	cran = "CSIndicators" 

	version("1.1.1", md5="0ac39730e04e5ac48d83dbcd4c6e6550")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-multiapply@2.1.1:", type=("build", "run"))
	depends_on("r-climprojdiags", type=("build", "run"))
	depends_on("r-cstools", type=("build", "run"))
	depends_on("r-spei", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-s2dv", type=("build", "run"))
