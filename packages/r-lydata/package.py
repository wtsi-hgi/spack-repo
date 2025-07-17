# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLydata(RPackage):
    """Example Dataset for crossmeta Package

    Raw data downloaded from GEO for the compound LY294002. Raw data is from multiple platforms from Affymetrix and Illumina. This data is used to illustrate the cross-platform meta-analysis of microarray data using the crossmeta package.
    """

    bioc = "lydata"

    version("1.34.0", commit="f000890c4682661f07e569d6557da7df467dc9eb")
    version("1.28.0", commit="477654a24d3e3887a1baf8ce91e93835f6252822")
