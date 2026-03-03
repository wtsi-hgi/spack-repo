# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWa(RPackage):
	"""While-Alive Loss Rate for Recurrent Event in the Presence of
Death

	Contains inferential and graphical routines for multi-group analysis of while-alive loss (or event) rate for possibly recurrent nonfatal event in the presence of death.
	"""
	
	homepage = "https://sites.google.com/view/lmaowisc/"
	cran = "WA" 

	version("1.0", md5="2d10f0602a5d555ef5abbee000700385")

	depends_on("r@2.10:", type=("build", "run"))
