# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkfe(RPackage):
	"""UK Flood Estimation

	Functions to implement the methods of the Flood Estimation Handbook (FEH), associated updates and the revitalised flood hydrograph model (ReFH). Currently the package uses NRFA peak flow dataset version 12.1. Aside from FEH functionality, further hydrological functions are available. Most of the methods implemented in this package are described in one or more of the following: "Flood Estimation Handbook", Centre for Ecology & Hydrology (1999, ISBN:0 948540 94 X). "Flood Estimation Handbook Supplementary Report No. 1", Kjeldsen (2007, ISBN:0 903741 15 7). "Regional Frequency Analysis - an approach based on L-moments", Hosking & Wallis (1997, ISBN: 978 0 521 01940 8). "Proposal of the extreme rank plot for extreme value analysis: with an emphasis on flood frequency studies", Hammond (2019, <doi:10.2166/nh.2019.157>). "Making better use of local data in flood frequency estimation", Environment Agency (2017, ISBN: 978 1 84911 387 8). "Sampling uncertainty of UK design flood estimation" , Hammond (2021, <doi:10.2166/nh.2021.059>). "Improving the FEH statistical procedures for flood frequency estimation", Environment Agency (2008, ISBN: 978 1 84432 920 5). "Low flow estimation in the United Kingdom", Institute of Hydrology (1992, ISBN 0 948540 45 1). Wallingford HydroSolutions, (2016, <http://software.hydrosolutions.co.uk/winfap4/Urban-Adjustment-Procedure-Technical-Note.pdf>). Data from the UK National River Flow Archive (<https://nrfa.ceh.ac.uk/>, terms and conditions: <https://nrfa.ceh.ac.uk/costs-terms-and-conditions>).
	"""
	
	cran = "UKFE" 

	version("0.3.4", md5="e965b804fbc7b365ee49cd36a3b18c4a")
	version("0.3.3", md5="ddf1d9464d718f4d997e0aef326c1d83")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
