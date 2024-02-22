# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcmeta(RPackage):
	"""Varying Coefficient Meta-Analysis

	Implements functions for varying coefficient meta-analysis methods. 
  These methods do not assume effect size homogeneity. Subgroup effect size 
  comparisons, general linear effect size contrasts, and linear models of 
  effect sizes based on varying coefficient methods can be used to describe 
  effect size heterogeneity. Varying coefficient meta-analysis methods do not 
  require the unrealistic assumptions of the traditional fixed-effect and 
  random-effects meta-analysis methods.  
  For details see:  Statistical Methods for Psychologists, Volume 5, <https://dgbonett.sites.ucsc.edu/>.
	"""
	
	homepage = "https://github.com/dgbonett/vcmeta"
	cran = "vcmeta" 

	version("1.2.0", md5="22b348dc29be34c77e84bd7fec6d8e9c")

	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
