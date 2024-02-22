# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmmr(RPackage):
	"""CEU Mass Mediator RESTful API

	CEU (CEU San Pablo University) Mass Mediator is an on-line tool for aiding researchers in 
  performing metabolite annotation. 'cmmr' (CEU Mass Mediator RESTful API) allows 
  for programmatic access in R: batch search, batch advanced search, MS/MS (tandem mass spectrometry) search, etc.
  For more information about the API Endpoint please go to <https://github.com/lzyacht/cmmr>.
	"""
	
	homepage = "https://github.com/lzyacht/cmmr"
	cran = "cmmr" 

	version("0.1.2", md5="8a3eda7c479ce5af9c5feb602e2eb0cf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-progress@1.2:", type=("build", "run"))
	depends_on("r-rjsonio@1.3.0:", type=("build", "run"))
