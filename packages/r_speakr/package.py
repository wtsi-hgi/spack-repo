# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeakr(RPackage):
	"""A Wrapper for the Phonetic Software 'Praat'

	It allows running 'Praat' scripts from R and it provides some
    wrappers for basic plotting. It also adds support for literate markdown
    tangling. The package is designed to bring reproducible phonetic research
    into R.
	"""
	
	homepage = "https://github.com/stefanocoretta/speakr"
	cran = "speakr" 

	version("3.2.2", md5="066632e9ea5d060a9b83545d345d0fc3")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-quarto", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
