# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubbprobe(RPackage):
    """Probe sequence data for microarrays of type mu11ksubb

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Mu11KsubB_probe_tab.
    """

    bioc = "mu11ksubbprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksubbprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksubbprobe/mu11ksubbprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="b04b483e16251b59e618fb406075b566697018c398781fc5271970da695e338d",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
