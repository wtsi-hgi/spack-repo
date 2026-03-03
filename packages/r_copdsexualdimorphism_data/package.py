# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopdsexualdimorphismData(RPackage):
	"""Data to support sexually dimorphic and COPD differential analysis for gene expression and methylation.

	Datasets to support COPDSexaulDimorphism Package.
	"""
	
	bioc = "COPDSexualDimorphism.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/COPDSexualDimorphism.data_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/COPDSexualDimorphism.data/COPDSexualDimorphism.data_1.38.0.tar.gz"]

	version("1.38.0", md5="d7cf1990679c90cbaf5250c4761effec")


