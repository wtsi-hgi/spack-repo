# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwilio(RPackage):
	"""An Interface to the Twilio API for R

	The Twilio web service provides an API for computer programs
    to interact with telephony. The included functions wrap the SMS and MMS 
    portions of Twilio's API, allowing users to send and receive text messages
    from R. See <https://www.twilio.com/docs/> for more information.
	"""
	
	homepage = "http://github.com/seankross/twilio"
	cran = "twilio" 

	version("0.1.0", md5="8bad25f0fad8ce73121ab4796064d8ca")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
