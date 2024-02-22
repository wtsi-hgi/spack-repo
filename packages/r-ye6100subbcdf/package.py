# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYe6100subbcdf(RPackage):
	"""ye6100subbcdf

	A package containing an environment representing the Ye6100subB.CDF file.
	"""
	
	bioc = "ye6100subbcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ye6100subbcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ye6100subbcdf/ye6100subbcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="ee9ec4bd941940745bad538d79bfeab4")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation