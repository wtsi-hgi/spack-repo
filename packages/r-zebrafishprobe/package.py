# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishprobe(RPackage):
    """Probe sequence data for microarrays of type zebrafish

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Zebrafish_probe_tab.
    """

    bioc = "zebrafishprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/zebrafishprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/zebrafishprobe/zebrafishprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="80e756fef3de0c05ade610ae69ca5d4e79a6cd10d1f79006862160d8b2f868dd",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
