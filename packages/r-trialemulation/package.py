# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrialemulation(RPackage):
	"""Causal Analysis of Observational Time-to-Event Data

	Implements target trial emulation methods to apply randomized
    clinical trial design and analysis in an observational setting. Using
    marginal structural models, it can estimate intention-to-treat and
    per-protocol effects in emulated trials using electronic health
    records. A description and application of the method can be found in
    Danaei et al (2013) <doi:10.1177/0962280211403603>.
	"""
	
	homepage = "https://causal-lda.github.io/TrialEmulation/"
	cran = "TrialEmulation" 

	version("0.0.3.8", md5="5c2e94d80507ceaaccfe0a8e72feaecc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@0.7.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-parglm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
