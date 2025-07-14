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

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="a7a4f7942b6c1ddc668979a9d2173459b9d71c201642289bd2543c9c1125db84")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-scanmir", type=("build", "run"))

