# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinfidataepic(RPackage):
    """Example data for the Illumina Methylation EPIC array

    Data from 3 technical replicates of the cell line GM12878 from the EPIC methylation array.
    """

    bioc = "minfiDataEPIC"

    version("1.34.0", commit="21744660cc5dc093f790aa6914ff5ba889362ab0")
    version("1.28.0", commit="e036f5dbaa7c8877b227b481b25a6eb4d3ce9a5a")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.21.2:", type=("build", "run"))
    depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
    depends_on("r-illuminahumanmethylationepicanno-ilm10b2-hg19", type=("build", "run"))
