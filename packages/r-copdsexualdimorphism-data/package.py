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

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="6ea73e5a85cad49f08ea04bc1694f80dba69e4b36df14c1d0bf3a87e4e717dd6")


