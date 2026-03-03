# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsDatabase(RPackage):
	"""'Amazon Web Services' Database Services

	Interface to 'Amazon Web Services' database services,
    including 'Relational Database Service' ('RDS'), 'DynamoDB' 'NoSQL'
    database, and more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.database" 

	version("0.5.0", md5="5599374fc566e12efe7dc2327f756b1b")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
