# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntiword(RPackage):
	"""Extract Text from Microsoft Word Documents

	Wraps the 'AntiWord' utility to extract text from Microsoft Word 
    documents. The utility only supports the old 'doc' format, not the new xml 
    based 'docx' format. Use the 'xml2' package to read the latter.
	"""
	
	homepage = "https://docs.ropensci.org/antiword/"
	cran = "antiword" 

	version("1.3.3", md5="19130d394d56facc2c97d660d9a1c4cf")

	depends_on("r-sys@2:", type=("build", "run"))
