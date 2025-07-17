# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBovineprobe(RPackage):
    """Probe sequence data for microarrays of type bovine

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Bovine_probe_tab.
    """

    bioc = "bovineprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bovineprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bovineprobe/bovineprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="31546a053baf33f494e74961e5b6a93a952aad6702baecacc8d1ead98a728a44",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
