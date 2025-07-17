# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoe430bprobe(RPackage):
    """Probe sequence data for microarrays of type moe430b

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MOE430B_probe_tab.
    """

    bioc = "moe430bprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moe430bprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moe430bprobe/moe430bprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="d1dd2d165fe1d3ed3c3a3141a9da1e980bc4d7c497aeaf14f82c5e22efe0f1db",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
