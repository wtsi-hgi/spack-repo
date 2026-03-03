# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrord(RPackage):
	"""Doubly-Robust Estimators for Ordinal Outcomes

	Efficient covariate-adjusted estimators of quantities that are useful for 
    establishing the effects of treatments on ordinal outcomes.
	"""
	
	homepage = "https://github.com/benkeser/drord"
	cran = "drord" 

	version("1.0.1", md5="7d5b3651c8cc512c5b4c741a95063cfd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
