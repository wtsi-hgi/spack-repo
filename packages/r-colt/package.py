# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColt(RPackage):
	"""Command-Line Color Themes

	
  A collection of command-line color styles based on the 'crayon'
  package. 'Colt' styles are defined in themes that can easily be switched, to
  ensure command line output looks nice on dark as well as light consoles.
	"""
	
	homepage = "https://github.com/s-fleck/colt"
	cran = "colt" 

	version("0.1.1", md5="a045fd1702bc6ad7586d5601662edfb6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
