# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpfr(RPackage):
	"""List Balancing for Reweighting and Population Synthesis

	Performs iterative proportional updating given a seed table and
  an arbitrary number of marginal distributions. This is commonly used in
  population synthesis, survey raking, matrix rebalancing, and other
  applications. For example, a household survey may be weighted to match the
  known distribution of households by size from the census. An origin/
  destination trip matrix might be balanced to match traffic counts.
  The approach used by this package is based on a paper from
  Arizona State University (Ye, Xin, et. al. (2009)
  <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.537.723&rep=rep1&type=pdf>).
  Some enhancements have been made to their work including primary and 
  secondary target balance/importance, general marginal agreement, and weight 
  restriction.
	"""
	
	homepage = "https://github.com/dkyleward/ipfr"
	cran = "ipfr" 

	version("1.0.2", md5="b8955499e7273aa3bfa6de5910fa6d29")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@0.5.1:", type=("build", "run"))
	depends_on("r-mlr@2.11:", type=("build", "run"))
