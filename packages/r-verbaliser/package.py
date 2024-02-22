# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerbaliser(RPackage):
	"""Make your Text Mighty Fine

	Turn R analysis outputs into full sentences, by writing vectors into in-sentence lists, pluralising words conditionally, spelling out numbers if they are at the start of sentences, writing out dates in full following US or UK style, and managing capitalisations in tidy data.
	"""
	
	homepage = "https://github.com/cararthompson/verbaliseR"
	cran = "verbaliseR" 

	version("0.1", md5="20109e960bc463572f46da662bcefad0")

	depends_on("r-stringr", type=("build", "run"))
