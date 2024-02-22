# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfpack(RPackage):
	"""Flexible Bayes Factor Testing of Scientific Expectations

	Implementation of default Bayes factors
    for testing statistical hypotheses under various statistical models. The package is
    intended for applied quantitative researchers in the
    social and behavioral sciences, medical research,
    and related fields. The Bayes factor tests can be
    executed for statistical models such as 
    univariate and multivariate normal linear models,
    correlation analysis, generalized linear models, special cases of 
    linear mixed models, survival models, relational
    event models. Parameters that can be tested are
    location parameters (e.g., group means, regression coefficients),
    variances (e.g., group variances), and measures of 
    association (e.g,. polychoric/polyserial/biserial/tetrachoric/product
    moments correlations), among others.
    The statistical underpinnings are
    described in 
    Mulder and Xin (2019) <DOI:10.1080/00273171.2021.1904809>,
    Mulder and Gelissen (2019) <DOI:10.1080/02664763.2021.1992360>,
    Mulder (2016) <DOI:10.1016/j.jmp.2014.09.004>,
    Mulder and Fox (2019) <DOI:10.1214/18-BA1115>,
    Mulder and Fox (2013) <DOI:10.1007/s11222-011-9295-3>,
    Boeing-Messing, van Assen, Hofman, Hoijtink, and Mulder (2017) <DOI:10.1037/met0000116>,
    Hoijtink, Mulder, van Lissa, and Gu, (2018) <DOI:10.31234/osf.io/v3shc>,
    Gu, Mulder, and Hoijtink, (2018) <DOI:10.1111/bmsp.12110>,
    Hoijtink, Gu, and Mulder, (2018) <DOI:10.1111/bmsp.12145>, and
    Hoijtink, Gu, Mulder, and Rosseel, (2018) <DOI:10.1037/met0000187>. When using the
    packages, please refer to Mulder et al. (2021) <DOI:10.18637/jss.v100.i18>.
	"""
	
	homepage = "https://github.com/jomulder/BFpack"
	cran = "BFpack" 

	version("1.2.3", md5="b9144073cb0e8ecc3c8f04e2c725ff29")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-bain", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-bergm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-qrm", type=("build", "run"))
