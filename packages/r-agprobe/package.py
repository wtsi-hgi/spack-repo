# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgprobe(RPackage):
    """Probe sequence data for microarrays of type ag

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was AG_probe_tab.
    """

    bioc = "agprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/agprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/agprobe/agprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="73f84a89036dd95a8ba1fd59dbb82b6264d6dd6702d36a91b226fccbaae2caee",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
