# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2probe(RPackage):
    """Probe sequence data for microarrays of type hgu133plus2

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-U133_Plus_2_probe_tab.
    """

    bioc = "hgu133plus2probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133plus2probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133plus2probe/hgu133plus2probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="ac69f81034177b08b14d192ed1bc214968bc7f318c5047db06b1a71d4d37aff5",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
