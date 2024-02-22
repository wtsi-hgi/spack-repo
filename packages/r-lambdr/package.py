# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLambdr(RPackage):
	"""Create a Runtime for Serving Containerised R Functions on 'AWS
Lambda'

	Runtime for serving containers that can execute R code on the 
    'AWS Lambda' serverless compute service <https://aws.amazon.com/lambda/>.
    Provides the necessary functionality for handling the various endpoints
    required for accepting new input and sending responses.
	"""
	
	homepage = "https://lambdr.mdneuzerling.com/"
	cran = "lambdr" 

	version("1.2.5", md5="fa417ea16df7a567eabb2f473e041378")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
