# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpa(RPackage):
	"""Convert Between Phonetic Alphabets

	Converts character vectors between phonetic
    representations.  Supports IPA (International Phonetic Alphabet),
    X-SAMPA (Extended Speech Assessment Methods Phonetic Alphabet), and
    ARPABET (used by the CMU Pronouncing Dictionary).
	"""
	
	homepage = "https://github.com/rossellhayes/ipa"
	cran = "ipa" 

	version("0.1.0", md5="88c00dac409b4a8b5a0108fe27a94f09")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
