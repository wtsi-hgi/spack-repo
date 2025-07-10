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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DrugVsDiseasedata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DrugVsDiseasedata/DrugVsDiseasedata_1.38.0.tar.gz"]

	version("1.38.0", sha256="b1d9719fe34b792236ac2b378362712e37f3ac00bc40ab456669a745a3d7e60d")

	depends_on("r@2.10:", type=("build", "run"))

