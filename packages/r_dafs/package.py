# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDafs(RPackage):
	"""Data Analysis for Forensic Scientists

	Data and miscellanea to support the book "Introduction to Data analysis with R for Forensic Scientists." This book was written by James Curran and published by CRC Press in 2010 (ISBN: 978-1-4200-8826-7).
	"""
	
	cran = "dafs" 

	version("1.0-38", md5="506593636af543850b954c1289bef88e")

	depends_on("r-s20x", type=("build", "run"))
