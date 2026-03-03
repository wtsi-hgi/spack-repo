# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNexus(RPackage):
	"""Sourcing Archaeological Materials by Chemical Composition

	Exploration and analysis of compositional data in the
    framework of Aitchison (1986, ISBN: 978-94-010-8324-9). This package
    provides tools for chemical fingerprinting and source tracking of
    ancient materials.
	"""
	
	homepage = "https://packages.tesselle.org/nexus/"
	cran = "nexus" 

	version("0.2.0", md5="52539b7800cbc9b1f7adeaa8ec145310")
	version("0.1.0", md5="495364ab1355e6f5be56889ca80ef430")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dimensio@0.6:", type=("build", "run"))
	depends_on("r-arkhe@1.6:", type=("build", "run"))
	depends_on("r-isopleuros@1.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
