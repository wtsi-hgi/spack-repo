# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymethyldata(RPackage):
    """Example dataset of input data for shinyMethyl

    Extracted data from 369 TCGA Head and Neck Cancer DNA methylation samples. The extracted data serve as an example dataset for the package shinyMethyl. Original samples are from 450k methylation arrays, and were obtained from The Cancer Genome Atlas (TCGA). 310 samples are from tumor, 50 are matched normals and 9 are technical replicates of a control cell line.
    """

    bioc = "shinyMethylData"

    version("1.28.0", commit="c70f362f6288bcb5383c3875d4c05ea96eadb18e")
    version("1.22.0", commit="05737b55d25d0844a76f2f37cf3744925f34f026")

    depends_on("r@3:", type=("build", "run"))
