# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicspcadata(RPackage):
    """Supporting data for package OMICsPCA

    Supporting data for package OMICsPCA
    """

    bioc = "OMICsPCAdata"

    version("1.26.0", commit="d235e9c380d108deffde61af43b2613bbd3cf0ac")
    version("1.20.0", commit="8b2188edf2bcc1d78845e561397d7e625315eb29")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
