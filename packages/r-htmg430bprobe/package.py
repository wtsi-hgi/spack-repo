# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430bprobe(RPackage):
    """Probe sequence data for microarrays of type htmg430b

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_MG-430B_probe_tab.
    """

    bioc = "htmg430bprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430bprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430bprobe/htmg430bprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="29229709d5a0b882e0f0e2d065b64e8631111f34755d0b8510f66e3782005ce1",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
