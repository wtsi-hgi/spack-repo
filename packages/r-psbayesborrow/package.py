# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsbayesborrow(RPackage):
	"""Bayesian Information Borrowing with Propensity Score Matching

	Hybrid control design is a way to borrow information from external controls to augment concurrent controls in a randomized controlled trial and is expected to overcome the feasibility issue when adequate randomized controlled trials cannot be conducted. A major challenge in the hybrid control design is its inability to eliminate a prior-data conflict caused by systematic imbalances in measured or unmeasured confounding factors between patients in the concurrent treatment/control group and external controls. To prevent the prior-data conflict, a combined use of propensity score matching and Bayesian commensurate prior has been proposed in the context of hybrid control design. The propensity score matching is first performed to guarantee the balance in baseline characteristics, and then the Bayesian commensurate prior is constructed while discounting the information based on the similarity in outcomes between the concurrent and external controls. 'psBayesborrow' is a package to implement the propensity score matching and the Bayesian analysis with commensurate prior, as well as to conduct a simulation study to assess operating characteristics of the hybrid control design, where users can choose design parameters in flexible and straightforward ways depending on their own application.
	"""
	
	cran = "psBayesborrow" 

	version("1.0.0", md5="f10f8ba3aaf86ce79e5497463824259e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-optmatch", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-overlapping", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
