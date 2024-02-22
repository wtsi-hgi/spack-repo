# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REwoc(RPackage):
	"""Escalation with Overdose Control

	An implementation of a variety of escalation with overdose control designs introduced by Babb, Rogatko and Zacks (1998) <doi:10.1002/(SICI)1097-0258(19980530)17:10%3C1103::AID-SIM793%3E3.0.CO;2-9>. It calculates the next dose as a clinical trial proceeds and performs simulations to obtain operating characteristics.
	"""
	
	homepage = "https://github.com/dnzmarcio/ewoc/"
	cran = "ewoc" 

	version("0.3.0", md5="e183c31c686f61e29ea9d64ff31f22bc")

	depends_on("r-formula@1.2.1:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda@0.18.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-dorng@1.7.1:", type=("build", "run"))
