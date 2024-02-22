# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgcdf(RPackage):
	"""agcdf

	A package containing an environment representing the AG.CDF file.
	"""
	
	bioc = "agcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/agcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/agcdf/agcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="5dd14bc6a6d2729f5e7b170105c78e48")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation