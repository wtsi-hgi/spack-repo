# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgaClinical(RPackage):
    """Clinical datasets from The Cancer Genome Atlas Project

    Package provides clinical datasets from The Cancer Genome Atlas Project for all cohorts types from http://gdac.broadinstitute.org/. Clinical data format is explained here https://wiki.nci.nih.gov/display/TCGA/Clinical+Data+Overview. Data from 2015-11-01 snapshot.
    """

    bioc = "RTCGA.clinical"

    version("20151101.38.0", commit="39abc65737ce6716fd7a4dec8be0abbe35cd5684")
    version("20151101.32.0", commit="c3e3be40eb56177d7ac38c193013aa326a3940be")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rtcga", type=("build", "run"))
