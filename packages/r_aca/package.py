# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAca(RPackage):
	"""Abrupt Change-Point or Aberration Detection in Point Series

	Offers an interactive function for the detection of breakpoints in series. 
	"""
	
	cran = "ACA" 

	version("1.1", md5="440366eae322247ff50a5ab94fec360c")

	depends_on("r@3.2.2:", type=("build", "run"))
