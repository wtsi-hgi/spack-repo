# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene10stv1probe(RPackage):
    """Probe sequence data for microarrays of type mogene10stv1

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was MoGene-1_0-st-v1_probe_tab.
    """

    bioc = "mogene10stv1probe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene10stv1probe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene10stv1probe/mogene10stv1probe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="caa819f71523ed941e2c09faa8ac0bc91f807cc73d78761bb66f88cd8cd356e2",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
