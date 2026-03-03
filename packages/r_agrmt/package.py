# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgrmt(RPackage):
	"""Calculate Concentration and Dispersion in Ordered Rating Scales

	Calculates concentration and dispersion in ordered rating scales. It implements various measures of concentration and dispersion to describe what researchers variably call agreement, concentration, consensus, dispersion, or polarization among respondents in ordered data. It also implements other related measures to classify distributions. In addition to a generic city-block based concentration measure and a generic dispersion measure, the package implements various measures, including van der Eijk's (2001) <DOI: 10.1023/A:1010374114305> measure of agreement A, measures of concentration by Leik, Tatsle and Wierman, Blair and Lacy, Kvalseth, Berry and Mielke, Reardon, and Garcia-Montalvo and Reynal-Querol. Furthermore, the package provides an implementation of Galtungs AJUS-system to classify distributions, as well as a function to identify the position of multiple modes.
	"""
	
	homepage = "http://agrmt.r-forge.r-project.org"
	cran = "agrmt" 

	version("1.42.12", md5="65564fd7338cfdc39d639c5d3018f6c2")

