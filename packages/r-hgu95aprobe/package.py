# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95aprobe(RPackage):
    """Probe sequence data for microarrays of type hgu95a

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG_U95A_probe_tab.
    """

    bioc = "hgu95aprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95aprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95aprobe/hgu95aprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="aaae162cfe56637fa2a5116605aea4c2b2ca849d378fccde3efbc58acb1b2f6a",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
