# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmapperdata(RPackage):
	"""Pre-processed data for use with the CellMapper package

	Experiment data package. Contains microarray data from several large expression compendia that have been pre-processed for use with the CellMapper package. This pre-processed data is recommended for routine searches using the CellMapper package.
	"""
	
	bioc = "CellMapperData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CellMapperData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CellMapperData/CellMapperData_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="bd25205761affe6b34b45f3c96aa16eaee3d59442dc3fad5453e944a490dbd8a")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-cellmapper", type=("build", "run"))

