# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdconcord(RPackage):
	"""Concordances for 'R Markdown'

	Supports concordances in 'R Markdown' 
  documents.  This currently allows the original source
  location in the '.Rmd' file of errors detected by 'HTML tidy'
  to be found more easily, and potentially allows forward
  and reverse search in 'HTML' and 'LaTeX' documents
  produced from 'R Markdown'.  The 'LaTeX' support
  has been included in the most recent development 
  version of the 'patchDVI' package.
	"""
	
	homepage = "https://github.com/dmurdoch/RmdConcord"
	cran = "RmdConcord" 

	version("0.3", md5="bcd513b56e8117a3747af23334cfe0fd")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr@1.42:", type=("build", "run"))
	depends_on("pandoc@2.11.3:", type=("build", "link", "run"))
