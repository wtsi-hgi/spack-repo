# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarfreq(RPackage):
	"""Response Adaptive Randomization with 'Frequentist' Approaches

	Provides functions and command-line user interface to generate allocation sequence 
             by response-adaptive randomization for clinical trials. The package currently supports 
             two families of frequentist response-adaptive randomization procedures, Doubly Adaptive 
             Biased Coin Design ('DBCD') and Sequential Estimation-adjusted Urn Model ('SEU'), for 
             binary and normal endpoints. One-sided proportion (or mean) difference and Chi-square 
             (or 'ANOVA') hypothesis testing methods are also available in the package to  facilitate 
             the inference for treatment effect. Additionally, the package provides comprehensive and 
             efficient tools to allow one to evaluate and  compare the performance of randomization 
             procedures and tests based on various criteria. For example, plots for relationship among 
             assumed treatment effects,  sample size, and power are provided. Five allocation functions 
             for 'DBCD' and six addition rule functions for 'SEU' are implemented to target allocations 
             such as 'Neyman', 'Rosenberger' Rosenberger et al. (2001) 
             <doi:10.1111/j.0006-341X.2001.00909.x> and 'Urn' allocations.
	"""
	
	cran = "RARfreq" 

	version("0.1.4", md5="ff7289a441b4780c2e0edaa74060b7b1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
