# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaCnv(RPackage):
    """CNV (Copy-number variation) datasets from The Cancer Genome Atlas Project

    Package provides CNV (based on Merge snp) datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Retrieving +Data+Using+the+Data+Matrix. Data from 2015-11-01 snapshot.
    """

    bioc = "RTCGA.CNV"

    version("1.36.0", commit="b68d798d4c605ccf9735985f5f3f74b06663beec")
    version("1.30.0", commit="ca1e744d8a90ea15b1d57fabc6834d6ef5c989e2")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
