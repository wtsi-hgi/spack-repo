# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGet(RPackage):
	"""Global Envelopes

	Implementation of global envelopes for a set of general d-dimensional vectors T
    in various applications. A 100(1-alpha)% global envelope is a band bounded by two
    vectors such that the probability that T falls outside this envelope in any of the d
    points is equal to alpha. Global means that the probability is controlled simultaneously
    for all the d elements of the vectors. The global envelopes can be used for graphical
    Monte Carlo and permutation tests where the test statistic is a multivariate vector or
    function (e.g. goodness-of-fit testing for point patterns and random sets, functional
    analysis of variance, functional general linear model, n-sample test of correspondence
    of distribution functions), for central regions of functional or multivariate data (e.g.
    outlier detection, functional boxplot) and for global confidence and prediction bands
    (e.g. confidence band in polynomial regression, Bayesian posterior prediction). See
    Myllymäki and Mrkvička (2023) <arXiv:1911.06583>,
    Myllymäki et al. (2017) <doi: 10.1111/rssb.12172>,
    Mrkvička and Myllymäki (2023) <doi: 10.1007/s11222-023-10275-7>,
    Mrkvička et al. (2017) <doi: 10.1007/s11222-016-9683-9>,
    Mrkvička et al. (2020) <doi: 10.14736/kyb-2020-3-0432>,
    Mrkvička et al. (2021) <doi: 10.1007/s11009-019-09756-y>,
    Mrkvička et al. (2022) <doi: 10.1002/sim.9236>,
    Mrkvička et al. (2016) <doi: 10.1016/j.spasta.2016.04.005>,
    Myllymäki et al. (2021) <doi: 10.1016/j.spasta.2020.100436>,
    Dai et al. (2022) <doi: 10.5772/intechopen.100124>, and
    Dvořák and Mrkvička (2022) <doi: 10.1007/s00180-021-01134-y>.
	"""
	
	homepage = "https://github.com/myllym/GET"
	cran = "GET" 

	version("1.0", md5="ebf6c7e53fe880df9756a59de9434616")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
