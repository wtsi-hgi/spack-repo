# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtratfocusprobe(RPackage):
    """Probe sequence data for microarrays of type htratfocus

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_Rat-Focus_probe_tab.
    """

    bioc = "htratfocusprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htratfocusprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htratfocusprobe/htratfocusprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="f13bda3e2bf58d63b272a377cc5f890f3f0b0eb38b7e6d34c2753d826f5ab7fb",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
