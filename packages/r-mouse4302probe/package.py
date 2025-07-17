# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302probe(RPackage):
    """Probe sequence data for microarrays of type mouse4302

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Mouse430_2_probe_tab.
    """

    bioc = "mouse4302probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse4302probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse4302probe/mouse4302probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="c1267793705f59426c2fcc18462f53a64ef645ca62b1647599ae8f8a924cb686",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
