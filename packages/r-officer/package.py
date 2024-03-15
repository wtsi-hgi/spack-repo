# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROfficer(RPackage):
	"""Manipulation of Microsoft Word and PowerPoint Documents

	Access and manipulate 'Microsoft Word', 'RTF' and 'Microsoft PowerPoint' documents from R. 
  The package focuses on tabular and graphical reporting from R; it also provides two functions
  that let users get document content into data objects. A set of functions 
  lets add and remove images, tables and paragraphs of text in new or existing documents. 
  The package does not require any installation of Microsoft products to be able to write Microsoft 
  files. 
	"""
	
	homepage = "https://ardata-fr.github.io/officeverse/"
	cran = "officer" 

	version("0.6.5", md5="439524d706d798240f5dc162aa5ca075")

	depends_on("r-zip@2.1:", type=("build", "run"))
	depends_on("r-xml2@1.1:", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-ragg", type=("build", "run"))
