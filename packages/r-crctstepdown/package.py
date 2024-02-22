# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrctstepdown(RPackage):
	"""Univariate Analysis of Cluster Trials with Multiple Outcomes

	Frequentist statistical inference for cluster randomised trials with
  multiple outcomes that controls the family-wise error rate and provides nominal
  coverage of confidence sets. A full description of the methods can be found in Watson et al. (2023) <doi:10.1002/sim.9831>.
	"""
	
	cran = "crctStepdown" 

	version("0.5.2", md5="0aa3910cc29e615a69e747391df49ab6")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-fastglm@0.0.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
