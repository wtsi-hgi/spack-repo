# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaninecdf(RPackage):
    """caninecdf

    A package containing an environment representing the Canine.cdf file.
    """

    bioc = "caninecdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/caninecdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/caninecdf/caninecdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="77d0132c1aceda260cc9a20aa153daf3d3367443132b189031b23246fc70f7b8",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
