# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelegansprobe(RPackage):
    """Probe sequence data for microarrays of type celegans

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was C_elegans_probe_tab.
    """

    bioc = "celegansprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/celegansprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/celegansprobe/celegansprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="0bb7c678a65e3b78d91389726589d51de7b5d5dc22832dd1f2f35fe446d46716",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
