# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreebird(RPackage):
	"""Estimation and Inference for High Dimensional Mediation and
Surrogate Analysis

	Estimates and provides inference for quantities that assess high dimensional mediation and potential surrogate markers including the direct effect of treatment, indirect effect of treatment, and the proportion of treatment effect explained by a surrogate/mediator; details are described in Zhou et al (2022) <doi:10.1002/sim.9352> and Zhou et al (2020) 
    <doi:10.1093/biomet/asaa016>. This package relies on the optimization software 'MOSEK', 
    <https://www.mosek.com>.
	"""
	
	cran = "freebird" 

	version("1.0", md5="fc8838cde5abafcaa6987b7b54890ad7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scalreg", type=("build", "run"))
	depends_on("r-rmosek", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
