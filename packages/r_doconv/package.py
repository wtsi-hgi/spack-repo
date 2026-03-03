# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoconv(RPackage):
	"""Document Conversion to 'PDF' or 'PNG'

	It provides the ability to generate images from documents
 of different types. Three main features are provided: functions for
 generating document thumbnails, functions for performing visual tests
 of documents and a function for updating fields and table of contents
 of a 'Microsoft Word' or 'RTF' document. In order to work, 'LibreOffice' must be
 installed on the machine and or 'Microsoft Word'. If the latter is
 available, it can be used to produce PDF documents or images
 identical to the originals; otherwise, 'LibreOffice' is used and
 the rendering can be sometimes different from the original
 documents.
	"""
	
	cran = "doconv" 

	version("0.3.2", md5="ce0a41ee33595ffd171e118bbb7c71c1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-locatexec", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
