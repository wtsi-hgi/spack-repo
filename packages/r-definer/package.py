# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDefiner(RPackage):
	"""Creates Define XML Documents

	Creates 'define.xml' documents used for regulatory 
    submissions based on spreadsheet metadata.  Can also help
    create metadata and generate HTML data explorer. 
	"""
	
	cran = "defineR" 

	version("0.0.4", md5="46182446c1b8fc91344ac4f674ba748c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-common", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xslt", type=("build", "run"))
	depends_on("r-reporter", type=("build", "run"))
	depends_on("r-libr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
