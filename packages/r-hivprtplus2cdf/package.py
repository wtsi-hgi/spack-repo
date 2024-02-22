# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHivprtplus2cdf(RPackage):
	"""hivprtplus2cdf

	A package containing an environment representing the HIV PRTPlus 2.CDF file.
	"""
	
	bioc = "hivprtplus2cdf" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hivprtplus2cdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hivprtplus2cdf/hivprtplus2cdf_2.18.0.tar.gz"]

	version("2.18.0", md5="143d9c2f5f328786bae7bb8dc4daf261")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation