# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicroplot(RPackage):
	"""Microplots (Sparklines) in 'LaTeX', 'Word', 'HTML', 'Excel'

	The microplot function writes a set of R graphics files to be used as
  microplots (sparklines) in tables in either 'LaTeX', 'HTML', 'Word',
  or 'Excel' files.  For 'LaTeX', we provide methods for the
  Hmisc::latex() generic function to construct 'latex' tabular
  environments which include the graphs.  These can be used directly
  with the operating system 'pdflatex' or 'latex' command, or by using
  one of 'Sweave', 'knitr', 'rmarkdown', or 'Emacs org-mode' as an
  intermediary.  For 'MS Word', the msWord() function uses the
  'flextable' package to construct 'Word' tables which include the
  graphs.  There are several distinct approaches for constructing HTML
  files.  The simplest is to use the msWord() function with argument
  filetype="html".  Alternatively, use either 'Emacs org-mode' or the
  htmlTable::htmlTable() function to construct an 'HTML' file
  containing tables which include the graphs.  See the documentation
  for our as.htmlimg() function.  For 'Excel' use on 'Windows', the
  file examples/irisExcel.xls includes 'VBA' code which brings the
  individual panels into individual cells in the spreadsheet.
  Examples in the examples and demo subdirectories are shown with
  'lattice' graphics, 'ggplot2' graphics, and 'base' graphics.
  Examples for 'LaTeX' include 'Sweave' (both 'LaTeX'-style and
  'Noweb'-style), 'knitr', 'emacs org-mode', and 'rmarkdown' input
  files and their 'pdf' output files.  Examples for 'HTML' include
  'org-mode' and 'Rmd' input files and their webarchive 'HTML' output
  files.  In addition, the as.orgtable() function can display a
  data.frame in an 'org-mode' document.  The examples for 'MS Word'
  (with either filetype="docx" or filetype="html") work with all
  operating systems.  The package does not require the installation of
  'LaTeX' or 'MS Word' to be able to write '.tex' or '.docx' files.
	"""
	
	cran = "microplot" 

	version("1.0-45", md5="0d5916c27f2dfec500a47717379caa84")

	depends_on("r-hmisc@4.1.1:", type=("build", "run"))
	depends_on("r-hh", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-flextable@0.5.11:", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
