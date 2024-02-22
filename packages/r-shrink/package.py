# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShrink(RPackage):
	"""Global, Parameterwise and Joint Shrinkage Factor Estimation

	The predictive value of a statistical model can often be improved
    by applying shrinkage methods. This can be achieved, e.g., by regularized
    regression or empirical Bayes approaches. Various types of shrinkage factors can
    also be estimated after a maximum likelihood. While global shrinkage modifies
    all regression coefficients by the same factor, parameterwise shrinkage factors
    differ between regression coefficients. With variables which are either highly
    correlated or associated with regard to contents, such as several columns of a
    design matrix describing a nonlinear effect, parameterwise shrinkage factors are
    not interpretable and a compromise between global and parameterwise shrinkage,
    termed 'joint shrinkage', is a useful extension. A computational shortcut to
    resampling-based shrinkage factor estimation based on DFBETA residuals can be
    applied. Global, parameterwise and joint shrinkage for models fitted by lm(),
    glm(), coxph(), or mfp() is available.
	"""
	
	homepage = "https://github.com/biometrician/shrink"
	cran = "shrink" 

	version("1.2.3", md5="7f330d4545bc34b364723a476b3c7e60")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-mfp", type=("build", "run"))
