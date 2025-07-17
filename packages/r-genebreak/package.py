# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenebreak(RPackage):
    """Gene Break Detection

    Recurrent breakpoint gene detection on copy number aberration profiles.
    """

    homepage = "https://github.com/stefvanlieshout/GeneBreak"
    bioc = "GeneBreak"

    version("1.38.0", commit="092168b7506807b0757df0f23e9dbc633da12aa8")
    version("1.32.0", commit="a5e80580c9883ae1405af7db338dff3319655377")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-qdnaseq", type=("build", "run"))
    depends_on("r-cghcall", type=("build", "run"))
    depends_on("r-cghbase", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
