# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSendgridr(RPackage):
	"""Mail Sender Using 'Sendgrid' Service

	Send email using 'Sendgrid' <https://sendgrid.com/> 
            mail API(v3) <https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api/authentication>.
	"""
	
	homepage = "https://github.com/mrchypark/sendgridr"
	cran = "sendgridr" 

	version("0.6.1", md5="5fc289a8387d3245d7108b782811381d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-emayili@0.7:", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
