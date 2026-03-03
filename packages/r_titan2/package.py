# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTitan2(RPackage):
	"""Threshold Indicator Taxa Analysis

	Uses indicator species scores across binary partitions of
  a sample set to detect congruence in taxon-specific changes of abundance
  and occurrence frequency along an environmental gradient as evidence of
  an ecological community threshold.  Relevant references include Baker and King 
  (2010) <doi:10.1111/j.2041-210X.2009.00007.x>, King and Baker (2010) 
  <doi:10.1899/09-144.1>, and Baker and King (2013) <doi:10.1899/12-142.1>.
	"""
	
	cran = "TITAN2" 

	version("2.4.3", md5="059bb7b8f40ceb4134efdcb7f8b7ccf3", url="https://cran.r-project.org/src/contrib/TITAN2_2.4.3.tar.gz")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
