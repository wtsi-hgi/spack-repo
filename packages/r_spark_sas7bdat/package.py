# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparkSas7bdat(RPackage):
	"""Read in 'SAS' Data ('.sas7bdat' Files) into 'Apache Spark'

	Read in 'SAS' Data ('.sas7bdat' Files) into 'Apache Spark' from R. 'Apache Spark' is an open source cluster computing framework available at <http://spark.apache.org>. This R package uses the 'spark-sas7bdat' 'Spark' package (<https://spark-packages.org/package/saurfang/spark-sas7bdat>) to import and process 'SAS' data in parallel using 'Spark'. Hereby allowing to execute 'dplyr' statements in parallel on top of 'SAS' data.
	"""
	
	homepage = "https://github.com/bnosac/spark.sas7bdat"
	cran = "spark.sas7bdat" 

	version("1.4", md5="38b37d10a535051011e5a4cbcd0511c8")

	depends_on("r-sparklyr@0.3:", type=("build", "run"))
