# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKomaletter(RPackage):
	"""Simply Beautiful PDF Letters from Markdown

	Write beautiful yet customizable letters in R Markdown and
  directly obtain the finished PDF. Smooth generation of PDFs is realized by
  'rmarkdown', the 'pandoc-letter' template and the 'KOMA-Script' letter class.
  'KOMA-Script' provides enhanced replacements for the standard 'LaTeX' classes
  with emphasis on typography and versatility. 'KOMA-Script' is particularly
  useful for international writers as it handles various paper formats well, 
  provides layouts for many common window envelope types (e.g. German, US, 
  French, Japanese) and lets you define your own layouts. The package comes 
  with a default letter layout based on 'DIN 5008B'.
	"""
	
	homepage = "https://rnuske.github.io/komaletter/"
	cran = "komaletter" 

	version("0.5.0", md5="e59b93d6bdf5c30778a7e79794109d15")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmarkdown@0.6:", type=("build", "run"))
