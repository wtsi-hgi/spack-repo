# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevtools(RPackage):
	"""Tools to Support Evidence Synthesis

	Researchers commonly need to summarize scientific information, a process known as 'evidence synthesis'. The first stage of a synthesis process (such as a systematic review or meta-analysis) is to download a list of references from academic search engines such as 'Web of Knowledge' or 'Scopus'. The traditional approach to systematic review is then to sort these data manually, first by locating and removing duplicated entries, and then screening to remove irrelevant content by viewing titles and abstracts (in that order). 'revtools' provides interfaces for each of these tasks. An alternative approach, however, is to draw on tools from machine learning to visualise patterns in the corpus. In this case, you can use 'revtools' to render ordinations of text drawn from article titles, keywords and abstracts, and interactively select or exclude individual references, words or topics.
	"""
	
	homepage = "https://revtools.net"
	cran = "revtools" 

	version("0.4.1", md5="464657bc255f06066acedff6ce964ec0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-modeltools", type=("build", "run"))
	depends_on("r-ngram", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
