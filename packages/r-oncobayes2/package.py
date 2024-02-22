# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncobayes2(RPackage):
	"""Bayesian Logistic Regression for Oncology Dose-Escalation Trials

	Bayesian logistic regression model with optional
  EXchangeability-NonEXchangeability parameter modelling for flexible
  borrowing from historical or concurrent data-sources. The safety model
  can guide dose-escalation decisions for adaptive oncology Phase I
  dose-escalation trials which involve an arbitrary number of
  drugs. Please refer to Neuenschwander et al. (2008)
  <doi:10.1002/sim.3230> and Neuenschwander et al. (2016)
  <doi:10.1080/19466315.2016.1174149> for details on the methodology.
	"""
	
	cran = "OncoBayes2" 

	version("0.8-9", md5="6283f37a08108b45531947e65be50211", url="https://cran.r-project.org/src/contrib/OncoBayes2_0.8-9.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.19.3:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1:", type=("build", "run"))
	depends_on("r-posterior@1.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-bayesplot@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.19:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
