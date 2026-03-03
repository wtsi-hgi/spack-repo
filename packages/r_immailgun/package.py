# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmailgun(RPackage):
	"""Send Emails using 'Mailgun'

	Send emails using the 'mailgun' api. To use this package you will need an account from <https://www.mailgun.com> .
	"""
	
	cran = "IMmailgun" 

	version("0.1.2", md5="a1e6eb3abe9a198b4fb51862d7dc0cc6")

	depends_on("r-httr", type=("build", "run"))
