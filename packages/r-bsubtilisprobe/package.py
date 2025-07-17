# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsubtilisprobe(RPackage):
    """Probe sequence data for microarrays of type bsubtilis

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Bsubtilis_probe_tab.
    """

    bioc = "bsubtilisprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bsubtilisprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bsubtilisprobe/bsubtilisprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="893317f491dd7a9d6433d71f5c9a4ec6b7853c4b795be54937c972adde86294d",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
