# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtrat230pmprobe(RPackage):
    """Probe sequence data for microarrays of type htrat230pm

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HT_Rat230_PM_probe_tab.
    """

    bioc = "htrat230pmprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htrat230pmprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htrat230pmprobe/htrat230pmprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="9e6c0e7edc73772208e29a727475fee863671f59e094e98be82c12899891fe76",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
