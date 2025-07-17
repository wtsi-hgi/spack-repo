# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtu34probe(RPackage):
    """Probe sequence data for microarrays of type rtu34

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RT-U34_probe_tab.
    """

    bioc = "rtu34probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rtu34probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rtu34probe/rtu34probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="1c32f7f14a9776e58918958906ea34dd423daf3853f9378e6e4316c32a4d9755",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
