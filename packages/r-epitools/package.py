# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitools(RPackage):
	"""Epidemiology Tools

	Tools for training and practicing epidemiologists including methods for two-way and multi-way contingency tables.
	"""
	
	cran = "epitools" 

	version("0.5-10.1", md5="5687c399ed86c5de206164cd449e42ba")

	depends_on("r@2.10:", type=("build", "run"))
