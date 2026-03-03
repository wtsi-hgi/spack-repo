# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsyllable(RPackage):
	"""Count Syllables in Character Vectors

	Counts syllables in character vectors for English words.  Imputes syllables as the number of vowel sequences for words not found.  
	"""
	
	homepage = "https://github.com/quanteda/nsyllable"
	cran = "nsyllable" 

	version("1.0.1", md5="3377b03df57397a9175617cd72122f96")

	depends_on("r@2.10:", type=("build", "run"))
