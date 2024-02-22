# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDictionary(RPackage):
	"""Retrieve the Dictionary Definitions of English Words

	An R interface to the 'Free Dictionary API' 
    <https://dictionaryapi.dev/>, 
    <https://github.com/meetDeveloper/freeDictionaryAPI>. Retrieve
    dictionary definitions for English words, as well 
    as additional information including phonetics, part of speech, origins, 
    audio pronunciation, example usage, synonyms and antonyms, returned in 
    'tidy' format for ease of use.
	"""
	
	homepage = "https://github.com/stevecondylios/dictionaRy"
	cran = "dictionaRy" 

	version("0.1.1", md5="01f49553c0cf93e4dd25d1ea79ecc9f1")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
