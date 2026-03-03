# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2glmm(RPackage):
	"""Computes R Squared for Mixed (Multilevel) Models

	The model R squared and semi-partial R squared for the linear and
    generalized linear mixed model (LMM and GLMM) are computed with confidence
    limits. The R squared measure from Edwards et.al (2008) <DOI:10.1002/sim.3429>
    is extended to the GLMM using penalized quasi-likelihood (PQL) estimation
    (see Jaeger et al. 2016 <DOI:10.1080/02664763.2016.1193725>). Three methods
    of computation are provided and described as follows. First, The
    Kenward-Roger approach. Due to some inconsistency between the 'pbkrtest'
    package and the 'glmmPQL' function, the Kenward-Roger approach in the
    'r2glmm' package is limited to the LMM. Second, The method introduced
    by Nakagawa and Schielzeth (2013) <DOI:10.1111/j.2041-210x.2012.00261.x>
    and later extended by Johnson (2014) <DOI:10.1111/2041-210X.12225>.
    The 'r2glmm' package only computes marginal R squared for the LMM and does
    not generalize the statistic to the GLMM; however, confidence limits and
    semi-partial R squared for fixed effects are useful additions. Lastly, an
    approach using standardized generalized variance (SGV) can be used for
    covariance model selection. Package installation instructions can be found
    in the readme file.
	"""
	
	homepage = "https://github.com/bcjaeger/r2glmm"
	cran = "r2glmm" 

	version("0.1.2", md5="93cfdb1043f254278c3b4617abd2be8f")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-afex", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
