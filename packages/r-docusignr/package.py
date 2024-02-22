# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocusignr(RPackage):
	"""Connect to 'DocuSign' API

	Connect to the 'DocuSign' Rest API <https://www.docusign.com/p/RESTAPIGuide/RESTAPIGuide.htm>, 
  which supports embedded signing, and sending of documents. 
	"""
	
	homepage = "https://github.com/CannaData/docuSignr"
	cran = "docuSignr" 

	version("0.0.3", md5="00dbc37050dbc8eec084515fb492539b")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
