# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImplyr(RPackage):
	"""R Interface for Apache Impala

	'SQL' back-end to 'dplyr' for Apache Impala, the massively
    parallel processing query engine for Apache 'Hadoop'. Impala enables
    low-latency 'SQL' queries on data stored in the 'Hadoop' Distributed
    File System '(HDFS)', Apache 'HBase', Apache 'Kudu', Amazon Simple 
    Storage Service '(S3)', Microsoft Azure Data Lake Store '(ADLS)', 
    and Dell 'EMC' 'Isilon'. See <https://impala.apache.org> for more
    information about Impala.
	"""
	
	homepage = "https://github.com/ianmcook/implyr"
	cran = "implyr" 

	version("0.5.0", md5="109411852212b3fc3ac3504c6e89a303")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dbi@1.1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dbplyr@2.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
