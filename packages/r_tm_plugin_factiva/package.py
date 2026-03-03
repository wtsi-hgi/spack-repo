# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginFactiva(RPackage):
	"""Import Articles from 'Factiva' Using the 'tm' Text Mining
Framework

	Provides a 'tm' Source to create corpora from
  articles exported from the Dow Jones 'Factiva' content provider as
  XML or HTML files. It is able to read both text content and meta-data
  information (including source, date, title, author, subject,
  geographical coverage, company, industry, and various
  provider-specific fields).
	"""
	
	homepage = "https://github.com/nalimilan/R.TeMiS"
	cran = "tm.plugin.factiva" 

	version("1.8", md5="766910d1be183e7a008317d5fc31853d")

	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm@0.7.2:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
