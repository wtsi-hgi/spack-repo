# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNembm(RPackage):
	"""Using Network Evolution Models to Generate Networks with
Selected Blockmodel Type

	To study network evolution models and different blockmodeling approaches. Various functions enable generating (temporal) networks with a selected blockmodel type, taking into account selected local network mechanisms. The development of this package is financially supported the Slovenian Research Agency (www.arrs.gov.si) within the research program P5<96>0168 and the research project J5-2557 (Comparison and evaluation of different approaches to blockmodeling dynamic networks by simulations with application to Slovenian co-authorship networks).
	"""
	
	cran = "nemBM" 

	version("1.00.01", md5="5793c2dd548c90340e3321f22898c423")

	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-blockmodeling", type=("build", "run"))
