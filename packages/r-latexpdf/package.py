# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatexpdf(RPackage):
	"""Convert Tables to PDF or PNG

	Converts table-like objects to stand-alone PDF or PNG.
 Can be used to embed tables and arbitrary content in PDF or Word
 documents. Provides a low-level R interface for creating 'LaTeX'
 code, e.g. command() and a high-level interface for creating PDF
 documents, e.g. as.pdf.data.frame(). Extensive customization is
 available via mid-level functions, e.g. as.tabular(). See also 
 'package?latexpdf'. Support for PNG is experimental; see
 'as.png.data.frame'. Adapted from 'metrumrg' 
 <https://r-forge.r-project.org/R/?group_id=1215>.
 Requires a compatible installation of 'pdflatex',
 e.g. <https://miktex.org/>.
	"""
	
	cran = "latexpdf" 

	version("0.1.8", md5="d2ab3673953257468988e1c720f1b4c0")

