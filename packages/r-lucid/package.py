# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLucid(RPackage):
	"""Printing Floating Point Numbers in a Human-Friendly Format

	Print vectors (and data frames) of floating point numbers
    using a non-scientific format optimized for human readers.  Vectors
    of numbers are rounded using significant digits, aligned at the
    decimal point, and all zeros trailing the decimal point are dropped.
    See: Wright (2016). Lucid: An R Package for Pretty-Printing Floating Point
    Numbers. In JSM Proceedings, Statistical Computing Section. Alexandria,
    VA: American Statistical Association. 2270-2279.
	"""
	
	homepage = "https://kwstat.github.io/lucid/"
	cran = "lucid" 

	version("1.8", md5="eb098e22e5e57cb86f392c8446a169ab")

	depends_on("r-nlme", type=("build", "run"))
