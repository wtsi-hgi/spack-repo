# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2diiData(RPackage):
	"""Datasets to Measure the Alignment of Corporate Loan Books with
Climate Goals

	These datasets support the implementation in R of the
    software 'PACTA' (Paris Agreement Capital Transition Assessment),
    which is a free tool that calculates the alignment between corporate
    lending portfolios and climate scenarios
    (<https://www.transitionmonitor.com/>). Financial institutions use
    'PACTA' to study how their capital allocation decisions align with
    climate change mitigation goals. Because both financial institutions
    and market data providers keep their data private, this package
    provides fake, public data to enable the development and use of
    'PACTA' in R.
	"""
	
	homepage = "https://rmi-pacta.github.io/r2dii.data/"
	cran = "r2dii.data" 

	version("0.5.0", md5="e84089dd27dff951a2fa13e3a9b6ff90")
	version("0.4.1", md5="4f28f888c7ece6c76676bd94b8578e78")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
