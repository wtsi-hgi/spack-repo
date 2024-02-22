# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpem(RPackage):
	"""S-system parameter estimation method.

	This package can optimize the parameter in S-system models given time
	series data"""

	bioc = "SPEM"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SPEM_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SPEM/SPEM_1.42.0.tar.gz"]

	version("1.42.0", md5="2b0ef40bd2428559cf559dfeb2a384f3")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
