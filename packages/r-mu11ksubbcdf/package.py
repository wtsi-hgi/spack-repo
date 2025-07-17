# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubbcdf(RPackage):
    """mu11ksubbcdf

    A package containing an environment representing the Mu11KsubB.CDF file.
    """

    bioc = "mu11ksubbcdf"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksubbcdf_2.18.0.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksubbcdf/mu11ksubbcdf_2.18.0.tar.gz",
    ]

    version(
        "2.18.0",
        sha256="7388570b9916a414ed5164e590d46e175fff0c074d0f59587ae3dd4000d652b5",
    )

    depends_on("r-annotationdbi", type=("build", "run"))
