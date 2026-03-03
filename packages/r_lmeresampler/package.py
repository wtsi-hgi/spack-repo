# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmeresampler(RPackage):
	"""Bootstrap Methods for Nested Linear Mixed-Effects Models

	Bootstrap routines for nested linear mixed effects models fit using
    either 'lme4' or 'nlme'. The provided 'bootstrap()' function implements the
    parametric, residual, cases, random effect block (REB), and wild bootstrap 
    procedures. An overview of these procedures can be found 
    in Van der Leeden et al. (2008) <doi: 10.1007/978-0-387-73186-5_11>, 
    Carpenter, Goldstein & Rasbash (2003) <doi: 10.1111/1467-9876.00415>,
    and Chambers & Chandra (2013) <doi: 10.1080/10618600.2012.681216>.
	"""
	
	homepage = "https://github.com/aloy/lmeresampler"
	cran = "lmeresampler" 

	version("0.2.4", md5="f320a4e49a85dfca825d7530fc34281e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlmeu", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-hlmdiag", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
