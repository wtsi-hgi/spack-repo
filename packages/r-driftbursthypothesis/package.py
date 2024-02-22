# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDriftbursthypothesis(RPackage):
	"""Calculates the Test-Statistic for the Drift Burst Hypothesis

	Calculates the T-Statistic for the drift burst hypothesis from the working paper Christensen, Oomen and Reno (2018) <DOI:10.2139/ssrn.2842535>. The authors' MATLAB code is available upon request, see: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2842535>.
	"""
	
	homepage = "https://github.com/emilsjoerup/DriftBurstHypothesis"
	cran = "DriftBurstHypothesis" 

	version("0.4.0.1", md5="c8087cd91489b7b19a1bdbfb4afedf9f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
