# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbci(RPackage):
	"""Robust Empirical Bayes Confidence Intervals

	Computes empirical Bayes confidence estimators and confidence
    intervals in a normal means model. The intervals are robust in the sense
    that they achieve correct coverage regardless of the distribution of the
    means. If the means are treated as fixed, the intervals have an average
    coverage guarantee. The implementation is based on Armstrong, Kolesár and
    Plagborg-Møller (2020) <arXiv:2004.03448>.
	"""
	
	homepage = "https://github.com/kolesarm/ebci"
	cran = "ebci" 

	version("1.0.0", md5="72ed3030caa2533110e961a4ade74f1b")

	depends_on("r@4.1:", type=("build", "run"))
