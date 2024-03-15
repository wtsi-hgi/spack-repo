# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdxpower(RPackage):
	"""Time to Event Outcome in Experimental Designs of Pre-Clinical
Studies

	Conduct simulation-based customized power calculation 
             for clustered time to event data in a mixed crossed/nested design,
             where a number of cell lines and a number of mice within each cell line are considered to achieve a desired statistical power,
             motivated by Eckel-Passow and colleagues (2021) <doi:10.1093/neuonc/noab137>.
             This package provides two commonly used models for powering a design, linear mixed effects and Cox frailty model. Both models account for
             within-subject (cell line) correlation while holding different distributional assumptions about the outcome. 
             Alternatively, the counterparts of fixed effects model are also available, which produces similar estimates of statistical power.
	"""
	
	cran = "PDXpower" 

	version("1.0.0", md5="1d0eec593a1799b5fe650f08272807a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-frailtypack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
