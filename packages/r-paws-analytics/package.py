# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsAnalytics(RPackage):
	"""'Amazon Web Services' Analytics Services

	Interface to 'Amazon Web Services' 'analytics' services,
    including 'Elastic MapReduce' 'Hadoop' and 'Spark' big data service,
    'Elasticsearch' search engine, and more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.analytics" 

	version("0.5.0", md5="23b00abb8daf49009070c5ad06d05dd7")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
