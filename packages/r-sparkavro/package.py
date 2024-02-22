# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkavro(RPackage):
	"""Load Avro file into 'Apache Spark'

	Load Avro Files into 'Apache Spark' using 'sparklyr'. This
    allows to read files from 'Apache Avro' <https://avro.apache.org/>.
	"""
	
	cran = "sparkavro" 

	version("0.3.0", md5="42ef0e7b422a626c3ed84dd44200bc9d")

	depends_on("r-sparklyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
