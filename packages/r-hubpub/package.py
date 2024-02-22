# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHubpub(RPackage):
	"""Utilities to create and use Bioconductor Hubs

	HubPub provides users with functionality to help with the Bioconductor Hub structures. The package provides the ability to create a skeleton of a Hub style package that the user can then populate with the necessary information. There are also functions to help add resources to the Hub package metadata files as well as publish data to the Bioconductor S3 bucket.
	"""
	
	bioc = "HubPub" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HubPub_1.10.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HubPub/HubPub_1.10.1.tar.gz"]

	version("1.10.1", md5="b69a4d04cd126e624ce9513040bc1abe")

	depends_on("r-available", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-biocthis", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
