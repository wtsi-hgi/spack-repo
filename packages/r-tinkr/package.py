# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinkr(RPackage):
	"""Cast '(R)Markdown' Files to 'XML' and Back Again

	Parsing '(R)Markdown' files with numerous regular expressions can
    be fraught with peril, but it does not have to be this way. Converting
    '(R)Markdown' files to 'XML' using the 'commonmark' package allows
    in-memory editing via of 'markdown' elements via 'XPath' through the
    extensible 'R6' class called 'yarn'. These modified 'XML' representations
    can be written to '(R)Markdown' documents via an 'xslt' stylesheet which
    implements an extended version of 'GitHub'-flavoured 'markdown' so that you
    can tinker to your hearts content.
	"""
	
	homepage = "https://docs.ropensci.org/tinkr/"
	cran = "tinkr" 

	version("0.2.0", md5="e51840670ecf4461020e47875cbe1ee7")

	depends_on("r-commonmark@1.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
