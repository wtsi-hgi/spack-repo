# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwrKinesis(RPackage):
	"""Amazon 'Kinesis' Consumer Application for Stream Processing

	Fetching data from Amazon 'Kinesis' Streams using the Java-based 'MultiLangDaemon' interacting with Amazon Web Services ('AWS') for easy stream processing from R. For more information on 'Kinesis', see <https://aws.amazon.com/kinesis>.
	"""
	
	homepage = "https://github.com/daroczig/AWR.Kinesis"
	cran = "AWR.Kinesis" 

	version("1.7.6", md5="40b35c4cd84f4690c0903c4e696aaaa1")

	depends_on("r-awr", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
