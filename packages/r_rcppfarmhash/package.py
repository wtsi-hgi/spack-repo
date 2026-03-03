# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppfarmhash(RPackage):
	"""Interface to the Google 'FarmHash' Family of Hash Functions

	The Google 'FarmHash' family of hash functions is used by
 the Google 'BigQuery' data warehouse via the 'FARM_FINGERPRINT'
 function. This package permits to calculate these hash digest
 fingerprints directly from R, and uses the included 'FarmHash'
 files written by G. Pike and copyrighted by Google, Inc.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppfarmhash/"
	cran = "RcppFarmHash" 

	version("0.0.3", md5="3226eda9710a4abfd9b07ddc7961003c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppint64", type=("build", "run"))
