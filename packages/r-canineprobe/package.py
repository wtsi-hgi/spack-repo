# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanineprobe(RPackage):
    """Probe sequence data for microarrays of type canine

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Canine_probe_tab.
    """

    bioc = "canineprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/canineprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/canineprobe/canineprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="c2762626e9349203008852b4b758bee9fffdac2c3e87dbd546a5bf45fbcae0f8",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
