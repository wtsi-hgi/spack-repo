# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaRppa(RPackage):
    """RPPA datasets from The Cancer Genome Atlas Project

    Package provides RPPA datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Protein+Array +Data+Format+Specification?src=search
    """

    bioc = "RTCGA.RPPA"

    version("1.36.0", commit="a0e9a422be7b521accf53e2e33e1eaaa702a5137")
    version("1.30.0", commit="d73a8d012513e8a9ce87e1f5e67d2cae238608eb")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
