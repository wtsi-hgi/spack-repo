# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsTranslate(RPackage):
	"""Client for 'AWS Translate'

	A client for 'AWS Translate' <https://aws.amazon.com/documentation/translate>, a machine translation service that will convert a text input in one language into a text output in another language.
	"""
	
	homepage = "https://github.com/cloudyr/aws.translate"
	cran = "aws.translate" 

	version("0.1.4", md5="39f4fb2255d3663cf3f0423d09690edc")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-aws-signature@0.3.4:", type=("build", "run"))
