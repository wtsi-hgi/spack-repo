# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManytests(RPackage):
	"""Multiple Testing Procedures of Cox (2011) and Wong and Cox
(2007)

	Performs the multiple testing procedures of Cox (2011) <doi:10.5170/CERN-2011-006> and Wong and Cox (2007) <doi:10.1080/02664760701240014>.
	"""
	
	cran = "ManyTests" 

	version("1.2", md5="c8889051cb6d2a79a15a06f3cbb1ac92")

