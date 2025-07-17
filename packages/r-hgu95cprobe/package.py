# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95cprobe(RPackage):
    """Probe sequence data for microarrays of type hgu95c

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U95C_probe_tab.
    """

    bioc = "hgu95cprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95cprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95cprobe/hgu95cprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="cd1db2bcddbeff5f82803fd3b0267ca5f14b7cfd1a16e9f87794ba0aa6f48b3e",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
