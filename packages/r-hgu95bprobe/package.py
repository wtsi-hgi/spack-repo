# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95bprobe(RPackage):
    """Probe sequence data for microarrays of type hgu95b

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U95B_probe_tab.
    """

    bioc = "hgu95bprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95bprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95bprobe/hgu95bprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="8fb1fa2026d26b2b8efacaffd2e461e2a94662d9f12199a29f52c00f2c1311f9",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
