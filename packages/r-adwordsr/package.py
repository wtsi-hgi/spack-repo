# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdwordsr(RPackage):
	"""Access the 'Google Adwords' API

	Allows access to selected services that are part of the 
    'Google Adwords' API <https://developers.google.com/adwords/api/docs/guides/start>.
	'Google Adwords' is an online advertising service by 'Google', that delivers Ads 
	to users. This package offers a authentication process using 'OAUTH2'.  Currently, 
	there are two methods of data of accessing the API, depending on the type of 
	request. One method uses 'SOAP' requests which require building an 'XML' structure 
	and then sent to the API. These are used for the 'ManagedCustomerService' and 
	the 'TargetingIdeaService'. The second method is by building 'AWQL' queries for 
	the reporting side of the 'Google Adwords' API.
	"""
	
	homepage = "https://www.branded3.com/"
	cran = "adwordsR" 

	version("0.3.1", md5="8ece6be0c6be8e8f53cf66cdfad1e615")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
