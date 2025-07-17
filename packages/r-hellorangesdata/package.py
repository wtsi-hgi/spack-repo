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

    version("1.34.0", commit="82ffbcd36346f97f03a9ea543f56625789e7c7c8")
    version("1.28.0", commit="df2a164845f71140f928058f28b4f91c3555af03")
