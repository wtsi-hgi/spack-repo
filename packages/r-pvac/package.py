# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvac(RPackage):
	"""PCA-based gene filtering for Affymetrix arrays

	The package contains the function for filtering genes by the proportion of variation accounted for by the first principal component (PVAC).
	"""
	
	bioc = "pvac" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pvac_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pvac/pvac_1.50.0.tar.gz"]

	version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="ad45217fa2fde5716abdbcd55fde000348b74ed8c76ebf58570f4f911a816a1c")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-affy@1.20:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
