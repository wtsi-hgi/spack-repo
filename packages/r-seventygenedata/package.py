# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeventygenedata(RPackage):
	"""ExpressionSets from the van't Veer and Van de Vijver breast cancer studies

	Gene expression data for the two breast cancer cohorts published by van't Veer and Van de Vijver in 2002.
	"""
	
	homepage = "https://bioconductor.org/packages/release/data/experiment/html/seventyGeneData.html"
	bioc = "seventyGeneData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/seventyGeneData_1.38.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/seventyGeneData/seventyGeneData_1.38.2.tar.gz"]

	version("1.38.2", md5="20fbac8869adfe019eeef340a209da1d")

	depends_on("r@2.13:", type=("build", "run"))

