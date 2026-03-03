# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterpdf(RPackage):
	"""Plot Raster Graphics in PDF Files

	The ability to plot raster graphics in PDF files can be useful
    when one needs multi-page documents, but the plots contain so many
    individual elements that (the usual) use of vector graphics results in
    inconveniently large file sizes. Internally, the package plots each
    individual page as a PNG, and then combines them in one PDF file.
	"""
	
	homepage = "https://ilarischeinin.github.io/rasterpdf"
	cran = "rasterpdf" 

	version("0.1.1", md5="68aa579933358f4491abbc3ba54ab333")

	depends_on("r-png", type=("build", "run"))
