# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGconsensus(RPackage):
	"""Consensus Value Constructor

	An implementation of the International Bureau of Weights and Measures (BIPM) generalized consensus estimators used to assign the reference value in a key comparison exercise. This can also be applied to any interlaboratory study. Given a set of different sources, primary laboratories or measurement methods this package provides an evaluation of the variance components according to the selected statistical method for consensus building. It also implements the comparison among different consensus builders and evaluates the participating method or sources against the consensus reference value. Based on a diverse set of references, DerSimonian-Laird (1986) <doi:10.1016/0197-2456(86)90046-2>, for a complete list of references look at the reference section in the package documentation.
	"""
	
	cran = "gconsensus" 

	version("0.3.2", md5="68026c70ab266ae2a785d6415cb635fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass@7:", type=("build", "run"))
	depends_on("r-rjags@4.8:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
