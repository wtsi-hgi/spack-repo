# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadiporna(RPackage):
    """A Curated RNA-Seq Dataset of MDI-induced Differentiated Adipocytes (3T3-L1)

    A curated dataset of RNA-Seq samples. The samples are MDI-induced pre-phagocytes (3T3-L1) at different time points/stage of differentiation. The package document the data collection, pre-processing and processing. In addition to the documentation, the package contains the scripts that was used to generated the data.
    """

    homepage = "https://github.com/MahShaaban/curatedAdipoRNA"
    bioc = "curatedAdipoRNA"

    version("1.24.0", commit="12247819288a24013adee4954aaf03ab0ace36b8")
    version("1.18.0", commit="a9918d69395c7c4d6e8ba7ccfee26e91cec5253f")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
