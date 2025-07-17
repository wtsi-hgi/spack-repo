# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RU133x3pprobe(RPackage):
    """Probe sequence data for microarrays of type u133x3p

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was U133_X3P_probe_tab.
    """

    bioc = "u133x3pprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/u133x3pprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/u133x3pprobe/u133x3pprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="1e8b1cc9514cb92affd60d60db3559af2b6dc683800fdaa00fb7a2e36633f577",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
