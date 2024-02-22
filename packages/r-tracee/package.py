# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracee(RPackage):
	"""Easily Save Output and Trace it Back to Code

	Write output (plots and tables) ensuring traceability back to code. Includes a graphics saver with simple automation of stamping with source, destination and creation time. A list of plots can be saved at once. A user-friendly selection of output dimensions for presentations, on-screen inspections, and more available.
	"""
	
	cran = "tracee" 

	version("0.0.4", md5="a357c013d5409ab60414655118a3eaa2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nmdata@0.0.14:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
