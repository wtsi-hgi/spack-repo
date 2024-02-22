# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginLexisnexis(RPackage):
	"""Import Articles from 'LexisNexis' Using the 'tm' Text Mining
Framework

	Provides a 'tm' Source to create corpora from
  articles exported from the 'LexisNexis' content provider as
  HTML files. It is able to read both text content and meta-data
  information (including source, date, title, author and pages).
  Note that the file format is highly unstable: there is no warranty
  that this package will work for your corpus, and you may have
  to adjust the code to adapt it to your particular format.
	"""
	
	homepage = "https://github.com/nalimilan/R.TeMiS"
	cran = "tm.plugin.lexisnexis" 

	version("1.4.1", md5="c57bea1a8b889bd2e0c24fe872380341")

	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-isocodes", type=("build", "run"))
