# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanmirdata(RPackage):
	"""miRNA Affinity models for the scanMiR package

	This package contains companion data to the scanMiR package. It contains `KdModel` (miRNA 12-mer binding affinity models) collections corresponding to all human, mouse and rat mirbase miRNAs. See the scanMiR package for details.
	"""
	
	bioc = "scanMiRData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/scanMiRData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/scanMiRData/scanMiRData_1.8.0.tar.gz"]

	version("1.8.0", md5="4c717492a3c85bbcf199873e35190219")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-scanmir", type=("build", "run"))

	# experiment