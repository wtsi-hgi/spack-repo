# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBondanalyst(RPackage):
	"""Methods for Fixed-Income Valuation, Risk and Return

	Bond Pricing and Fixed-Income Valuation of Selected Securities included here serve as a quick reference of Quantitative Methods for undergraduate courses on Fixed-Income and CFA Level I Readings on Fixed-Income Valuation, Risk and Return.
    CFA Institute ("CFA Program Curriculum 2020 Level I Volumes 1-6. (Vol. 5, pp. 107-151, pp. 237-299)", 2019, ISBN: 9781119593577).
    Barbara S. Petitt ("Fixed Income Analysis", 2019, ISBN: 9781119628132).
    Frank J. Fabozzi ("Handbook of Finance: Financial Markets and Instruments", 2008, ISBN: 9780470078143).
    Frank J. Fabozzi ("Fixed Income Analysis", 2007, ISBN: 9780470052211).
	"""
	
	cran = "bondAnalyst" 

	version("1.0.1", md5="98d22df1f7c9d0c4e0f7ecf3b223965c")

	depends_on("r-rdpack", type=("build", "run"))
