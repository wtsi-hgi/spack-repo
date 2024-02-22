# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalaeosig(RPackage):
	"""Significance Tests for Palaeoenvironmental Reconstructions

	Several tests of quantitative palaeoenvironmental reconstructions 
  from microfossil assemblages, including the null model tests of the 
  statistically significant of reconstructions developed by Telford and Birks
  (2011) <doi:10.1016/j.quascirev.2011.03.002>, and tests of the effect of 
  spatial autocorrelation on transfer function model performance using methods 
  from Telford and Birks (2009) <doi:10.1016/j.quascirev.2008.12.020> and 
  Trachsel and Telford (2016) <doi:10.5194/cp-12-1215-2016>. Age-depth models with 
  generalized mixed-effect regression from Heegaard et al (2005)
  <doi:10.1191/0959683605hl836rr> are also included.
	"""
	
	homepage = "https://github.com/richardjtelford/palaeoSig"
	cran = "palaeoSig" 

	version("2.1-3", md5="e0fa5e68e3e653244e7bd34238e7287e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-rioja", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-assertr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
