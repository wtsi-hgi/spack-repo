# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS3Resourcer(RPackage):
	"""S3 Resource Resolver

	A S3 resource is provided by Amazon Web Services S3 or a S3-compatible object store (such as Minio). 
    The resource can be a tidy file to be downloaded from the object store, or a data lake (such as Delta Lake) 
    Parquet file to be read by Apache Spark.
	"""
	
	cran = "s3.resourcer" 

	version("1.1.1", md5="9523ec85fc039b37d7b7334d73699ef3")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-resourcer@1.2:", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
