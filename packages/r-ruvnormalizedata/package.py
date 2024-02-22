# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvnormalizedata(RPackage):
	"""Gender data for the RUVnormalize package

	Microarray gene expression data from the study of Vawter et al., 2004.
	"""
	
	bioc = "RUVnormalizeData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/RUVnormalizeData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/RUVnormalizeData/RUVnormalizeData_1.22.0.tar.gz"]

	version("1.22.0", md5="5d7104746a5cac16500870312dd769a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

	# experiment