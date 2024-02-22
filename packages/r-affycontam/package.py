# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffycontam(RPackage):
	"""structured corruption of affymetrix cel file data.

	structured corruption of cel file data to demonstrate QA
	effectiveness"""

	bioc = "affyContam"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/affyContam_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/affyContam/affyContam_1.60.0.tar.gz"]

	version("1.60.0", md5="eb7e98d31e923d77d4e6197e5cf8b02d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affydata", type=("build", "run"))
