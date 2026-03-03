# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLccr(RPackage):
	"""Latent Class Capture-Recapture Models

	Estimation of latent class models with individual covariates for capture-recapture data. See Forcina and Bartolucci (2021)<arxiv:2106.03811>.
	"""
	
	cran = "LCCR" 

	version("1.3", md5="4f830fcbfee6e89039647a166b73bbde")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
