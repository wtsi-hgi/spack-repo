# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRRsp(RPackage):
	"""Dynamic Generation of Scientific Reports

	The RSP markup language makes any text-based document come alive.  RSP provides a powerful markup for controlling the content and output of LaTeX, HTML, Markdown, AsciiDoc, Sweave and knitr documents (and more), e.g. 'Today's date is <%=Sys.Date()%>'.  Contrary to many other literate programming languages, with RSP it is straightforward to loop over mixtures of code and text sections, e.g. in month-by-month summaries.  RSP has also several preprocessing directives for incorporating static and dynamic contents of external files (local or online) among other things.  Functions rstring() and rcat() make it easy to process RSP strings, rsource() sources an RSP file as it was an R script, while rfile() compiles it (even online) into its final output format, e.g. rfile('report.tex.rsp') generates 'report.pdf' and rfile('report.md.rsp') generates 'report.html'.  RSP is ideal for self-contained scientific reports and R package vignettes.  It's easy to use - if you know how to write an R script, you'll be up and running within minutes.
	"""
	
	homepage = "https://henrikbengtsson.github.io/R.rsp/"
	cran = "R.rsp" 

	version("0.46.0", md5="fadc1d1c2acab2967dce3b537f6f2f2a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-r-methodss3@1.8:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
