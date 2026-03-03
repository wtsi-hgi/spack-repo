# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrpostman(RPackage):
	"""An IMAP Client for R

	An easy-to-use IMAP client that provides tools for message searching,
    selective fetching of message attributes, mailbox management, attachment extraction, 
    and several other IMAP features, paving the way for e-mail data analysis in R.
	"""
	
	homepage = "https://allanvc.github.io/mRpostman/"
	cran = "mRpostman" 

	version("1.1.2", md5="c4fa4eca8eecedeaba55b1f9b34b65e1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
