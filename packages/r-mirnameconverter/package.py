# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnameconverter(RPackage):
    """Convert miRNA Names to Different miRBase Versions

    Translating mature miRNA names to different miRBase versions, sequence retrieval, checking names for validity and detecting miRBase version of a given set of names (data from http://www.mirbase.org/).
    """

    bioc = "miRNAmeConverter"

    version("1.36.0", commit="a3c5a5ddfc0d3e0f71f44631a6f84ca95575d901")
    version("1.30.0", commit="40e10f7d2f304ff06ea0435608d9dd468f8a07bf")

    depends_on("r-mirbaseversions-db", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
