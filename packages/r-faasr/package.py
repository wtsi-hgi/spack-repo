# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaasr(RPackage):
	"""FaaS (Function as a Service) Package

	Allows users to create and deploy the workflow with multiple functions
    in Function-as-a-Service (FaaS) cloud computing platforms.
    The 'FaaSr' package makes it simpler for R developers to use FaaS platforms by providing the following functionality:
    1) Parsing and validating a JSON-based payload compliant to 'FaaSr' schema supporting multiple FaaS platforms
    2) Invoking user functions written in R in a Docker container (derived from rocker), using a list generated from
       the parser as argument
    3) Downloading/uploading of files from/to S3 buckets using simple primitives
    4) Logging to files in S3 buckets
    5) Triggering downstream actions supporting multiple FaaS platforms
    6) Generating FaaS-specific API calls to simplify the registering of a user's workflow with a FaaS platform
    Supported FaaS platforms:
    Apache OpenWhisk <https://openwhisk.apache.org/>
    GitHub Actions <https://github.com/features/actions>
    Amazon Web Services (AWS) Lambda <https://aws.amazon.com/lambda/>
    Supported cloud data storage for persistent storage:
    Amazon Web Services (AWS) Simple Storage Service (S3) <https://aws.amazon.com/s3/>.
	"""
	
	homepage = "https://github.com/FaaSr/FaaSr-package"
	cran = "FaaSr" 

	version("1.1.2", md5="42e9903a43d109ec1ea14a6d52d477f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-paws-application-integration", type=("build", "run"))
	depends_on("r-paws-compute", type=("build", "run"))
	depends_on("r-paws-storage", type=("build", "run"))
	depends_on("r-paws-security-identity", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
