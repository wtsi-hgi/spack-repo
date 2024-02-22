# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCreditas(RPackage):
	"""Generate CRediT Author Statements

	A tiny package to generate CRediT author statements (<https://credit.niso.org/>). 
    It provides three functions: create a template, read it back and generate the CRediT author statement in a text file.
	"""
	
	homepage = "https://github.com/ropensci/CRediTas/"
	cran = "CRediTas" 

	version("0.2.0", md5="98f495bad0f1ed46f0a9efdc86715765")

