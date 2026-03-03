# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcumos(RPackage):
	"""'Acumos' R Interface

	Create, upload and run 'Acumos' R models.
  'Acumos' (<https://www.acumos.org>) is a platform and open source framework intended to make it easy to build,
  share, and deploy AI apps. 'Acumos' is part of the 'LF AI Foundation', an umbrella
  organization within 'The Linux Foundation'. With this package, user can create a
  component, and push it to an 'Acumos' platform.
	"""
	
	homepage = "https://www.acumos.org"
	cran = "acumos" 

	version("0.4-4", md5="43f591bdbe451d108ac59d91182b0afc")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rprotobuf", type=("build", "run"))
	depends_on("r-rserve", type=("build", "run"))
	depends_on("r-restrserve", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
