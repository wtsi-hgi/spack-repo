# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDineq(RPackage):
	"""Decomposition of (Income) Inequality

	Decomposition of (income) inequality by population sub groups. 
    For a decomposition on a single variable the mean log deviation can be used
      (see Mookherjee Shorrocks (1982) <DOI:10.2307/2232673>).
    For a decomposition on multiple variables a regression based technique can be 
      used (see Fields (2003) <DOI:10.1016/s0147-9121(03)22001-x>).
    Recentered influence function regression for marginal effects of the (income 
      or wealth) distribution  (see Firpo et al. (2009) <DOI:10.3982/ECTA6822>).
    Some extensions to inequality functions to handle weights and/or missings.
	"""
	
	cran = "dineq" 

	version("0.1.0", md5="adb51fcb16459e463c7a7c085e709545")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot@1.3.20:", type=("build", "run"))
	depends_on("r-hmisc@4.0.3:", type=("build", "run"))
