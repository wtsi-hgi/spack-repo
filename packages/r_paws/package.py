# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaws(RPackage):
	"""Amazon Web Services Software Development Kit

	Interface to Amazon Web Services <https://aws.amazon.com>,
    including storage, database, and compute services, such as 'Simple
    Storage Service' ('S3'), 'DynamoDB' 'NoSQL' database, and 'Lambda'
    functions-as-a-service.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws" 

	version("0.5.0", md5="8499c55e77d9fd8d10480b43c2120885")

	depends_on("r-paws-analytics@0.5:", type=("build", "run"))
	depends_on("r-paws-application-integration@0.5:", type=("build", "run"))
	depends_on("r-paws-common@0.6:", type=("build", "run"))
	depends_on("r-paws-compute@0.5:", type=("build", "run"))
	depends_on("r-paws-cost-management@0.5:", type=("build", "run"))
	depends_on("r-paws-customer-engagement@0.5:", type=("build", "run"))
	depends_on("r-paws-database@0.5:", type=("build", "run"))
	depends_on("r-paws-developer-tools@0.5:", type=("build", "run"))
	depends_on("r-paws-end-user-computing@0.5:", type=("build", "run"))
	depends_on("r-paws-machine-learning@0.5:", type=("build", "run"))
	depends_on("r-paws-management@0.5:", type=("build", "run"))
	depends_on("r-paws-networking@0.5:", type=("build", "run"))
	depends_on("r-paws-security-identity@0.5:", type=("build", "run"))
	depends_on("r-paws-storage@0.5:", type=("build", "run"))
