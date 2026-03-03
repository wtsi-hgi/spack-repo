# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkrplotr(RPackage):
	"""Display Resizable Plots

	Display a plot in a Tk canvas.
	"""
	
	cran = "tkRplotR" 

	version("0.1.7", md5="648b4068649979818b7d76e98237455b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("tcl@8.6:", type=("build", "link", "run"))
	depends_on("tk@8.6:", type=("build", "link", "run"))
