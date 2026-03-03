# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrtf(RPackage):
	"""Transformation Trees and Forests

	Recursive partytioning of transformation models with
  corresponding random forest for conditional transformation models 
  as described in 'Transformation Forests' (Hothorn and Zeileis, 2021, <doi:10.1080/10618600.2021.1872581>) 
  and 'Top-Down Transformation Choice' (Hothorn, 2018, <DOI:10.1177/1471082X17748081>).
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "trtf" 

	version("0.4-2", md5="a2f0c6ed63d7e12131f3176b9615c034")

	depends_on("r-mlt@1.4.1:", type=("build", "run"))
	depends_on("r-partykit@1.2.1:", type=("build", "run"))
	depends_on("r-tram", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-variables", type=("build", "run"))
	depends_on("r-libcoin", type=("build", "run"))
