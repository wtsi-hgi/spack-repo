# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdmulti(RPackage):
	"""Analysis of RD Designs with Multiple Cutoffs or Scores

	The regression discontinuity (RD) design is a popular quasi-experimental design for causal inference and policy evaluation. The 'rdmulti' package provides tools to analyze RD designs with multiple cutoffs or scores: rdmc() estimates pooled and cutoff specific effects for multi-cutoff designs, rdmcplot() draws RD plots for multi-cutoff designs and rdms() estimates effects in cumulative cutoffs or multi-score designs. See Cattaneo, Titiunik and Vazquez-Bare (2020) <https://rdpackages.github.io/references/Cattaneo-Titiunik-VazquezBare_2020_Stata.pdf> for further methodological details. 
	"""
	
	cran = "rdmulti" 

	version("1.1", md5="2102ee6beaf8ff79f8a9944682ce5d68")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdrobust", type=("build", "run"))
