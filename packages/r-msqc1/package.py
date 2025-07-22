# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsqc1(RPackage):
    """Sigma mix MSQC1 data

    contains eight technical replicate data set and a three replicate dilution series of the MS Qual/Quant Quality Control Mix standard sample (Sigma-Aldrich, Buchs, Switzerland) measured on five different mass spectrometer platforms at the Functional Genomics Center Zurich.
    """

    homepage = "https://panoramaweb.org/labkey/MSQC1.url"
    bioc = "msqc1"

    version("1.36.0", commit="3c9fe74135f34168f0760318c7d78fce7c6a2329")
    version("1.30.0", commit="17e718a818d59161568d13ba73a6b202e562e2c9")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
