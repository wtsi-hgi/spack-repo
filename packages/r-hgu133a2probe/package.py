# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133a2probe(RPackage):
    """Probe sequence data for microarrays of type hgu133a2

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U133A_2_probe_tab.
    """

    bioc = "hgu133a2probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133a2probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133a2probe/hgu133a2probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="33490e59a21e2af8b53095a71b819bc71bed4a637de3a6b9ff55d62992333a2a",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
