# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWheatprobe(RPackage):
    """Probe sequence data for microarrays of type wheat

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was wheat_probe_tab.
    """

    bioc = "wheatprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/wheatprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/wheatprobe/wheatprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="885b76ecf9803fc986bd7c7bda9bd6b5388a4f9fe0f3164d192fb7bfef882eba",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
