# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapp(RPackage):
	"""Easily Build Command Line Applications

	Run simple 'R' scripts as command line applications, with
  automatic robust and convenient support for command line arguments.
  This package provides 'Rapp', an alternative 'R' front-end similar to 
  'Rscript', that enables this.
	"""
	
	cran = "Rapp" 

	version("0.1.0", md5="d8de253c0b31aedd792e2c8d523ad035")

	depends_on("r-yaml", type=("build", "run"))
