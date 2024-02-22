# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYe6100subacdf(RPackage):
	"""ye6100subacdf

	A package containing an environment representing the Ye6100subA.CDF file.
	"""
	
	bioc = "ye6100subacdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ye6100subacdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ye6100subacdf/ye6100subacdf_2.18.0.tar.gz"]

	version("2.18.0", md5="27bd71410956bfe8bffc8de14b85bdb0")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation