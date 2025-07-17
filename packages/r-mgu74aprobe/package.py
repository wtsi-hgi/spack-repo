# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74aprobe(RPackage):
    """Probe sequence data for microarrays of type mgu74a

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74A_probe_tab.
    """

    bioc = "mgu74aprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74aprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74aprobe/mgu74aprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="71e99abbc79db4ef3916f2040c6f9365533699fb7cd6902c5650255db8d02320",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
