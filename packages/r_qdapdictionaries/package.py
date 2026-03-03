# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdapdictionaries(RPackage):
	"""Dictionaries and Word Lists for the 'qdap' Package

	A collection of text analysis dictionaries and word lists for use with
        the 'qdap' package.
	"""
	
	homepage = "http://trinker.github.com/qdapDictionaries/"
	cran = "qdapDictionaries" 

	version("1.0.7", md5="c13ecac0bc2171ef0df713f7502d1e48")

	depends_on("r@3:", type=("build", "run"))
