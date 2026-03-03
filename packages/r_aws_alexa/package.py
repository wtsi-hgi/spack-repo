# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsAlexa(RPackage):
	"""Client for the Amazon Alexa Web Information Services API

	Use the Amazon Alexa Web Information Services API to
    find information about domains, including the kind of content
    that they carry, how popular are they---rank and traffic history,
    sites linking to them, among other things. See <https://aws.amazon.com/awis/>
    for more information.
	"""
	
	cran = "aws.alexa" 

	version("0.1.8", md5="e4ebc7646a54793f436e8f3d78a5efdf")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-aws-signature", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
