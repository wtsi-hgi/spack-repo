# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSendmailr(RPackage):
	"""Send Email Using R

	Package contains a simple SMTP client with minimal dependencies which 
        provides a portable solution for sending email, including file attachments and inline html reports, 
        from within R. SMTP Authentication and SSL/STARTTLS is implemented using curl.
	"""
	
	homepage = "https://github.com/olafmersmann/sendmailR"
	cran = "sendmailR" 

	version("1.4-0", md5="b8a5eccd3a787dad249d81e192d46c05")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
