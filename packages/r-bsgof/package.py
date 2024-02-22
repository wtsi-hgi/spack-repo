# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgof(RPackage):
	"""Birnbaum-Saunders Goodness-of-Fit Test

	Performs goodness of fit test for the Birnbaum-Saunders distribution and provides the maximum likelihood estimate and the method-of-moments estimate. For more details, see Park and Wang (2013) <arXiv:2308.10150>. This work was supported by the National Research Foundation of Korea (NRF) grants funded by the Korea government (MSIT) (No. 2022R1A2C1091319, RS-2023-00242528).
	"""
	
	homepage = "https://AppliedStat.GitHub.io/R/"
	cran = "bsgof" 

	version("0.23.8", md5="df24acb01a650eaa027846d6a642066e")

	depends_on("r@4:", type=("build", "run"))
