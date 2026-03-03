# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXva(RPackage):
	"""Calculates Credit Risk Valuation Adjustments

	Calculates a number of valuation adjustments including CVA, DVA,
    FBA, FCA, MVA and KVA. A two-way margin agreement has been implemented. For
    the KVA calculation three regulatory frameworks are supported: CEM, (simplified) SA-CCR, OEM
	and IMM. The probability of default is implied through the credit spreads curve.
    The package supports an exposure calculation based on SA-CCR which includes several trade types
    and a simulated path which is currently available only for IRSwaps. The latest regulatory capital charge methodologies
    have been implementing including BA-CVA & SA-CVA.
	"""
	
	homepage = "https://openriskcalculator.com/"
	cran = "xVA" 

	version("1.1", md5="42b2968d50a35514f1d27c643d4201cc")

	depends_on("r-saccr", type=("build", "run"))
	depends_on("r-trading", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
