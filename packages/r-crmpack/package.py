# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrmpack(RPackage):
	"""Object-Oriented Implementation of CRM Designs

	Implements a wide range of model-based dose
    escalation designs, ranging from classical and modern continual
    reassessment methods (CRMs) based on dose-limiting toxicity endpoints to
    dual-endpoint designs taking into account a biomarker/efficacy outcome. The
    focus is on Bayesian inference, making it very easy to setup a new design
    with its own JAGS code. However, it is also possible to implement 3+3
    designs for comparison or models with non-Bayesian estimation. The whole
    package is written in a modular form in the S4 class system, making it very
    flexible for adaptation to new models, escalation or stopping rules.
	"""
	
	homepage = "https://github.com/roche/crmPack"
	cran = "crmPack" 

	version("1.0.5", md5="ac4b5a789f3bee31eadd349d7927dca6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
