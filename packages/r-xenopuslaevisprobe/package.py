# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXenopuslaevisprobe(RPackage):
    """Probe sequence data for microarrays of type xenopuslaevis

    This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was Xenopus_laevis_probe_tab.
    """

    bioc = "xenopuslaevisprobe"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/xenopuslaevisprobe_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/xenopuslaevisprobe/xenopuslaevisprobe_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="fc02bcffec01db3aff71f74e28df1a9685f26ce84178c011ee6f3f613f092b5f",
    )

    depends_on("r@1.6:", type=("build", "run"))
    depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))
