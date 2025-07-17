# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinfidata(RPackage):
    """Example data for the Illumina Methylation 450k array

    Data from 6 samples across 2 groups from 450k methylation arrays.
    """

    bioc = "minfiData"

    version("0.54.0", commit="71d3467bf63394decdd7b421df8b1a8674bee713")
    version("0.48.0", commit="dc941ff89bceff00e33c88f7af0c0307641b5616")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-minfi@1.21.2:", type=("build", "run"))
    depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
    depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19", type=("build", "run"))
