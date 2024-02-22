# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugvsdiseasedata(RPackage):
	"""Drug versus Disease Data

	Data package which provides default disease expression profiles, clusters and annotation information for use with the DrugVsDisease package.
	"""
	
	bioc = "DrugVsDiseasedata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/DrugVsDiseasedata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/DrugVsDiseasedata/DrugVsDiseasedata_1.38.0.tar.gz"]

	version("1.38.0", md5="40b800653aab57e822a18afe5bd1a2e7")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment