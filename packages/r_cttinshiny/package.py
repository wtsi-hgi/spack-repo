# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCttinshiny(RPackage):
	"""Shiny Interface for the CTT Package

	A Shiny interface developed in close coordination with the CTT package, providing a GUI that guides the user through CTT analyses.
	"""
	
	cran = "CTTinShiny" 

	version("0.1.0", md5="fa0ab648d7244b59f7aaddb410500a52")

	depends_on("r-ctt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
