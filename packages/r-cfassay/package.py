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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CFAssay_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CFAssay/CFAssay_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="44a819139501cf2bee863a9d0a0e624f19c9a3e0a2cc6755f2020a7e886e133a")

	depends_on("r@2.10:", type=("build", "run"))
