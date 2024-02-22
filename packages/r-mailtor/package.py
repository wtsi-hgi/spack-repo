# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMailtor(RPackage):
	"""Creates a Friendly User Interface for Emails Sending in 'shiny'

	Allows the user to generate a friendly user interface for emails sending. 
    The user can choose from the most popular free email services ('Gmail', 'Outlook', 'Yahoo') and his default email application. 
    The package is a wrapper for the 'Mailtoui' 'JavaScript' library.  See <https://mailtoui.com/#menu> for more information. 
	"""
	
	homepage = "https://github.com/feddelegrand7/mailtoR"
	cran = "mailtoR" 

	version("0.1.0", md5="2aeef4aee74864b65dbfd0967161313f")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
