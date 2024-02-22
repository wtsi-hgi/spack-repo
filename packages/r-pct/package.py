# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPct(RPackage):
	"""Propensity to Cycle Tool

	Functions and example data to teach and
  increase the reproducibility of the methods and code underlying 
  the Propensity to Cycle Tool (PCT), a research project and web application 
  hosted at <https://www.pct.bike/>. 
  For an academic paper on the methods,
  see Lovelace et al (2017) <doi:10.5198/jtlu.2016.862>.
	"""
	
	homepage = "https://itsleeds.github.io/pct/"
	cran = "pct" 

	version("0.9.9", md5="0dd47c9760e7ea122e10602a71cf955a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-stplanr@0.2.8:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
