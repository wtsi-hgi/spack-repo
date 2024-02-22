# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaccr(RPackage):
	"""SA Counterparty Credit Risk under CRR2

	Computes the Exposure-At-Default based on  the standardized approach
    of CRR2 (SA-CCR). The simplified version of SA-CCR has been included, as well as the OEM methodology.
	Multiple trade types of all the five major asset classes are being supported including the 'Other' Exposure and, given the inheritance-
    based structure of the application, the addition of further trade types
    is straightforward. The application returns a list of trees per Counterparty and CSA after
    automatically separating the trades based on the Counterparty, the CSAs, the hedging sets, the
    netting sets and the risk factors. The basis and volatility transactions are
    also identified and treated in specific hedging sets whereby the corresponding 
    penalty factors are applied. All the examples appearing on the
    regulatory papers (both for the margined and the un-margined workflow) have been
    implemented including the latest CRR2 developments.
	"""
	
	homepage = "https://openriskcalculator.com/"
	cran = "SACCR" 

	version("3.2", md5="83fc2becfb763ae31b0eb09eab053d7c")

	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-trading", type=("build", "run"))
