# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarcode(RPackage):
	"""Render Barcode Distribution Plots

	The function code{barcode()}
        produces a histogram-like plot of a distribution that shows
        granularity in the data.
	"""
	
	cran = "barcode" 

	version("1.3.0", md5="a883ea45532a634763386b5f41d4b6b3")

	depends_on("r-lattice", type=("build", "run"))
