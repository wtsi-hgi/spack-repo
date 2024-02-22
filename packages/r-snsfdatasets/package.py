# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnsfdatasets(RPackage):
	"""Download Datasets from the Swiss National Science Foundation
(SNF, FNS, SNSF)

	Download and read datasets from the Swiss National
     Science Foundation (SNF, FNS, SNSF; <https://snf.ch>).  The
     package is lightweight and without dependencies.  Downloaded
     data can optionally be cached, to avoid repeated downloads of
     the same files.  There are also utilities for comparing
     different versions of datasets, i.e. to report added, removed
     and changed entries.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/SNSFdatasets/"
	cran = "SNSFdatasets" 

	version("0.1.1", md5="0a65d9497567787dd7ff7b5483c644cf")

