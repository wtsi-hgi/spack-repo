# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkbq(RPackage):
	"""Google 'BigQuery' Support for 'sparklyr'

	A 'sparklyr' extension package providing an integration with Google 'BigQuery'.
  It supports direct import/export where records are directly streamed from/to 'BigQuery'.
  In addition, data may be imported/exported via intermediate data extracts on Google 'Cloud Storage'.
	"""
	
	homepage = "http://www.mirai-solutions.com"
	cran = "sparkbq" 

	version("0.1.1", md5="775ce3b9b485e8e44415957af3a3fb98")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-sparklyr@0.7:", type=("build", "run"))
	depends_on("spark@2.2.0:", type=("build", "link", "run"))
