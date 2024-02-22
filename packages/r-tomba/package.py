# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomba(RPackage):
	"""Official R Library for Tomba Email Finder

	Email Finder R Client Library.
        Search emails are based on the website You give one domain name and it returns all the email addresses found on the internet.
        Email Finder generates or retrieves the most likely email address from a domain name, a first name and a last name.
        Email verify checks the deliverability of a given email address, verifies if it has been found in our database, and returns their sources.
	"""
	
	homepage = "https://tomba.io/"
	cran = "tomba" 

	version("1.0.1", md5="458c997dbe9641676e58e454d3ccff5c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
