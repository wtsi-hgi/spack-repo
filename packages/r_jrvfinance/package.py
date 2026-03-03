# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJrvfinance(RPackage):
	"""Basic Finance; NPV/IRR/Annuities/Bond-Pricing; Black Scholes

	Implements the basic financial analysis
    functions similar to (but not identical to) what
    is available in most spreadsheet software. This
    includes finding the IRR and NPV of regularly
    spaced cash flows and annuities. Bond pricing and
    YTM calculations are included. In addition, Black
    Scholes option pricing and Greeks are also
    provided.
	"""
	
	homepage = "https://github.com/jrvarma/jrvFinance"
	cran = "jrvFinance" 

	version("1.4.3", md5="84533a53311edb75ad34da761f1868a8")

	depends_on("r@3:", type=("build", "run"))
