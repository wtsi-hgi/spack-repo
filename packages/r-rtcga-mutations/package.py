# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaMutations(RPackage):
    """Mutations datasets from The Cancer Genome Atlas Project

    Package provides mutations datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Mutations data format is explained here https://wiki.nci.nih.gov/display/TCGA/Mutation+Annotation+Format+(MAF)+Specification. There is extra one column with patients' barcodes. Data from 2015-11-01 snapshot.
    """

    bioc = "RTCGA.mutations"

    version("20151101.38.0", commit="1d21fef8cb07410d6b82f3e5d7badb4ff3fc767a")
    version("20151101.32.0", commit="33cfd4eac108e61346b5a433b8c413ea625e0391")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
