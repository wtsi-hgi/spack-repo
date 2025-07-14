# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHellorangesdata(RPackage):
	"""Data for the HelloRanges tutorial vignette

	Provides the data that were used in the bedtools tutorial by Aaron Quinlan (http://quinlanlab.org/tutorials/bedtools/bedtools.html). Includes a subset of the DnaseI hypersensitivity data from "Maurano et al. Systematic Localization of Common Disease-Associated Variation in Regulatory DNA. Science. 2012. Vol. 337 no. 6099 pp. 1190-1195." The rest of the tracks were originally downloaded from the UCSC table browser. See the HelloRanges vignette for a port of the bedtools tutorial to R.
	"""
	
	bioc = "HelloRangesData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HelloRangesData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HelloRangesData/HelloRangesData_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="ac5b8c4baed1b6123fcb0361df21d7da6748e9480189ef84da5aee6233675926")


