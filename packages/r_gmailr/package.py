# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmailr(RPackage):
	"""Access the 'Gmail' 'RESTful' API

	An interface to the 'Gmail' 'RESTful' API.  Allows access to
    your 'Gmail' messages, threads, drafts and labels.
	"""
	
	homepage = "https://gmailr.r-lib.org"
	cran = "gmailr" 

	version("2.0.0", md5="ab1e971c92c87e3528efc3414d4c7321")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-gargle@1.5.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
