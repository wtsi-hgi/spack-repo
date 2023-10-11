# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RConfintr(RPackage):
    """Calculates classic and/or bootstrap confidence intervals for many parameters such as the population mean, variance, interquartile range (IQR), median absolute deviation (MAD), skewness, kurtosis, Cramer's V, odds ratio, R-squared, quantiles (incl. median), proportions, different types of correlation measures, difference in means, quantiles and medians. Many of the classic confidence intervals are described in Smithson, M. (2003, ISBN: 978-0761924999). Bootstrap confidence intervals are calculated with the R package 'boot'. Both one- and two-sided intervals are supported."""

    homepage = "https://github.com/mayer79/confintr"
    cran = "confintr"

    version("1.0.2", sha256="7a104a2e7ef43405e70013bc99529a28bfe4cc4b61cdcc7dddc73426a665293e")
    version("1.0.1", sha256="3f4694a607b888b149e6bc73f711647a33d5066f07ce686e7e022d4fdd0a535c")
    version("1.0.0", sha256="0fb9333cec88780f2c90b2079434f2b5c23b98c7325c3ecf5c98f022f16a7a97")
    version("0.2.0", sha256="6f315e8bd01d79701f30dd7c31267b216a284dd53dead607b2d856edcbcef7fe")
    version("0.1.2", sha256="26f708c250c7f959a859e7018c46df64401afc4d0e39290c48f79d8ba1148419")
    version("0.1.1", sha256="949539699cce0d7344dd4359c9013a10111a6f10bb6702e881110e422f7bd3a2")
    version("0.1.0", sha256="cac47eea3afb6990a3a4d85989144992840daa92c8e0bc3b845326b54ee412b5")

    depends_on("r-boot", type=("build", "run"))
    depends_on("r-knitr", type=("run"))
    depends_on("r-rmarkdown", type=("run"))
    depends_on("r-testthat", type=("run"))
