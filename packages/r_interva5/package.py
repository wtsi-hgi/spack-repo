# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterva5(RPackage):
	"""Replicate and Analyse 'InterVA5'

	Provides an R version of the 'InterVA5' software (<http://www.byass.uk/interva/>) for coding cause of death from verbal autopsies. It also provides simple graphical representation of individual and population level statistics.
	"""
	
	cran = "InterVA5" 

	version("1.1.3", md5="74714c6c85c9f7265a2d9a0956b4ba31", url="https://cran.r-project.org/src/contrib/InterVA5_1.1.3.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
