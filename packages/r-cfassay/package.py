# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfassay(RPackage):
	"""Statistical analysis for the Colony Formation Assay

	The package provides functions for calculation of linear-quadratic cell survival curves and for ANOVA of experimental 2-way designs along with the colony formation assay.
	"""
	
	bioc = "CFAssay" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CFAssay_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CFAssay/CFAssay_1.36.0.tar.gz"]

	version("1.36.0", md5="122c969248ffd92330d93a266db6cb3c")

	depends_on("r@2.10:", type=("build", "run"))
