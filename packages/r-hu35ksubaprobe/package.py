# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubaprobe(RPackage):
    """Probe sequence data for microarrays of type hu35ksuba

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Hu35KsubA_probe_tab.
    """

    bioc = "hu35ksubaprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubaprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubaprobe/hu35ksubaprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="05cc4b223f4ec0f88266538710254f93b24cbbaed65e1fde72eeb1c60764da36",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
