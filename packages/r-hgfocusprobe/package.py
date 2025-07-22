# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgfocusprobe(RPackage):
    """Probe sequence data for microarrays of type hgfocus

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was HG-Focus_probe_tab.
    """

    bioc = "hgfocusprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgfocusprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgfocusprobe/hgfocusprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="82651bafddc9168e37fc57c0837d76fa4b24ad286ec54166a7bac6f0849c3f3a",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
