# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74bv2probe(RPackage):
    """Probe sequence data for microarrays of type mgu74bv2

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MG-U74Bv2_probe_tab.
    """

    bioc = "mgu74bv2probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74bv2probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74bv2probe/mgu74bv2probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="86ea30c85ecfc1ea45f1deac20eea9aef5fd109b94747fde95404ea01329c4ce",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
