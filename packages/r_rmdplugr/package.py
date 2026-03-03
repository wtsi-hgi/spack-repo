# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdplugr(RPackage):
	"""Plugins for R Markdown Formats

	Formats for R Markdown that undo modifications by
    'pandoc' and 'rmarkdown' to original 'latex' templates, such as
    smaller margins, paragraph spacing, and compact titles. In addition, 
    enhancements such as author blocks with affiliations and
    headers and footers are introduced. All of this functionality is built 
    around plugins that modify the default 'pandoc' template without relying on 
    custom templates.
	"""
	
	homepage = "https://github.com/jolars/rmdplugr"
	cran = "rmdplugr" 

	version("0.4.1", md5="58f4c56e9e4a652c64975de41ca50ae2")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
