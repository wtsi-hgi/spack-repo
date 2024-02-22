# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWheatcdf(RPackage):
	"""wheatcdf

	A package containing an environment representing the wheat.cdf file.
	"""
	
	bioc = "wheatcdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/wheatcdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/wheatcdf/wheatcdf_2.18.0.tar.gz"]

	version("2.18.0", md5="0abeeeb9700b8d93a1a83769bdd8480f")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation