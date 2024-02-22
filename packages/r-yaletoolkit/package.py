# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYaletoolkit(RPackage):
	"""Data Exploration Tools from Yale University

	This collection of data exploration tools was developed at
    Yale University for the graphical exploration of complex
    multivariate data; barcode and gpairs now have their own
    packages.  The big.read.table() function provided here may be
    useful for large files when only a subset is needed (but please
    see the note in the help page for this function).
	"""
	
	cran = "YaleToolkit" 

	version("4.2.3", md5="a390dd855985f28f8d4e21e141798973")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
