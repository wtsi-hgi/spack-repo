# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitrusprobe(RPackage):
    """Probe sequence data for microarrays of type citrus

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Citrus_probe_tab.
    """

    bioc = "citrusprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/citrusprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/citrusprobe/citrusprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="07ad0cd13bbe36fb2336efc3c025c8db5badb0d77c0449f4e39d991158e4c12d",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
