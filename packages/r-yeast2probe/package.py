# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeast2probe(RPackage):
    """Probe sequence data for microarrays of type yeast2

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Yeast_2_probe_tab.
    """

    bioc = "yeast2probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/yeast2probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/yeast2probe/yeast2probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="67b57da850a4b08645df2ea7877263ef6d95dc09e95b6b01eb95e1918c8bb688",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
