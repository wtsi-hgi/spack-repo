# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlfs(RPackage):
	"""Machine Learning Forest Simulator

	Climate-sensitive forest simulator based on the principles of 
  machine learning. It stimulates all key processes in the forest: radial growth, 
  height growth, mortality, crown recession, regeneration and harvesting. The 
  method for predicting tree heights was described by Skudnik and Jevšenak
  (2022) <doi:10.1016/j.foreco.2022.120017>, while the method for predicting
  basal area increments (BAI) was described by Jevšenak and Skudnik (2021) 
  <doi:10.1016/j.foreco.2020.118601>.
	"""
	
	cran = "MLFS" 

	version("0.4.2", md5="e865fe572451fb85e35b865c782a75e7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-brnn@0.6:", type=("build", "run"))
	depends_on("r-ranger@0.13.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-pscl@1.5.5:", type=("build", "run"))
	depends_on("r-naivebayes@0.9.7:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
