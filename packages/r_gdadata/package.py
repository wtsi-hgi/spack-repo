# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdadata(RPackage):
	"""Datasets for the Book Graphical Data Analysis with R

	Datasets used in the book 'Graphical Data Analysis with R' (Antony Unwin, CRC Press 2015).
	"""
	
	cran = "GDAdata" 

	version("0.93", md5="c77334bba4815c06fe31290b262c9a9f")

	depends_on("r@2.10:", type=("build", "run"))
