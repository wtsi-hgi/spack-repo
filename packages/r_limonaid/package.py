# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLimonaid(RPackage):
	"""Working with 'LimeSurvey' Surveys and Responses

	'LimeSurvey' is Free/Libre Open Source Software for
  the development and administrations of online studies, using
  sophisticated tailoring capabilities to support multiple study
  designs (see <https://www.limesurvey.org>). This package supports
  programmatic creation of surveys that can then be imported into
  'LimeSurvey', as well as user friendly import of responses from
  'LimeSurvey' studies.
	"""
	
	homepage = "https://r-packages.gitlab.io/limonaid"
	cran = "limonaid" 

	version("0.1.5", md5="5fcd22e8faed33856a284b85d479609e")

	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
