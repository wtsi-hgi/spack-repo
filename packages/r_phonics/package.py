# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhonics(RPackage):
	"""Phonetic Spelling Algorithms

	Provides a collection of phonetic algorithms including
    Soundex, Metaphone, NYSIIS, Caverphone, and others.  The package is
    documented in <doi:10.18637/jss.v095.i08>.
	"""
	
	homepage = "https://jameshoward.us/phonics-in-r/"
	cran = "phonics" 

	version("1.3.10", md5="61b362569fcee1083f2dea6ecd6e09f9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
