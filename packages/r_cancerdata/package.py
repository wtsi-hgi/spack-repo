# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancerdata(RPackage):
	"""Development and validation of diagnostic tests from high-dimensional molecular data: Datasets

	Dataset for the R package cancerclass
	"""
	
	bioc = "cancerdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/cancerdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/cancerdata/cancerdata_1.40.0.tar.gz"]

	version("1.40.0", md5="7baa088ef320a0222a897987ea8c3e8b")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

