# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubcprobe(RPackage):
    """Probe sequence data for microarrays of type hu35ksubc

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Hu35KsubC_probe_tab.
    """

    bioc = "hu35ksubcprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubcprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubcprobe/hu35ksubcprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="ab6e9a247be341fe7ec08f9706190e5289dd0f8b99a3a42ea7d9db8f0f2142e8",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
