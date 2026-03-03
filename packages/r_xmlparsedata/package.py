# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXmlparsedata(RPackage):
	"""Parse Data of 'R' Code as an 'XML' Tree

	Convert the output of 'utils::getParseData()' to an 'XML'
    tree, that one can search via 'XPath', and easier to manipulate in
    general.
	"""
	
	homepage = "https://github.com/r-lib/xmlparsedata#readme"
	cran = "xmlparsedata" 

	version("1.0.5", md5="3667d2785071e956227798e2a4cfbd49")

	depends_on("r@3:", type=("build", "run"))
