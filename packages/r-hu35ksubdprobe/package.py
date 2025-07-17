# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubdprobe(RPackage):
    """Probe sequence data for microarrays of type hu35ksubd

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Hu35KsubD_probe_tab.
    """

    bioc = "hu35ksubdprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubdprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubdprobe/hu35ksubdprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="dc885de57ea083205f1b61624a85c9ab87ad30cbeb70ebb84cc272f36eeb3bee",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
