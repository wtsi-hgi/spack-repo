# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarinerdata(RPackage):
	"""ExperimentHub data for the mariner package

	Subsampled Hi-C in HEK cells expressing the NHA9 fusion with an F to S mutated IDR ("FS") or without any mutations to the IDR ("Wildtype" or "WT"). These files are used for testing mariner functions and some examples.
	"""
	
	bioc = "marinerData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/marinerData_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/marinerData/marinerData_1.2.0.tar.gz"]

	version("1.2.0", md5="7875113ebb6baaaed6eb6fc762ba92ca")

	depends_on("r-experimenthub", type=("build", "run"))

