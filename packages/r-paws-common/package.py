# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsCommon(RPackage):
	"""Paws Low-Level Amazon Web Services API

	Functions for making low-level API requests to Amazon Web Services
    <https://aws.amazon.com>. The functions handle building, signing, and
    sending requests, and receiving responses. They are designed to help build 
    higher-level interfaces to individual services, such as Simple Storage
    Service (S3).
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.common" 

	version("0.7.1", md5="9af459e0fbfbcc2232325db0e839a834")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
