# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMrna(RPackage):
    """mRNA datasets from The Cancer Genome Atlas Project

    Package provides mRNA datasets from The Cancer Genome Atlas Project for all available cohorts types from http://gdac.broadinstitute.org/. Data format is explained here https://wiki.nci.nih.gov/display/TCGA/Gene+expression+data Data from 2015-11-01 snapshot.
    """

    bioc = "RTCGA.mRNA"

    version("1.36.0", commit="91cd9ce4bd4273448c2e304d0d8a421dcf1c02ea")
    version("1.30.0", commit="5e81af72c42787c8a3d52339de23c15eeb5c7e98")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
