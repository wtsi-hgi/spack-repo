# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlagme(RPackage):
    """Analysis of Metabolomics GC/MS Data

    Fragment-level analysis of gas chromatography-massspectrometry metabolomics data.
    """

    bioc = "flagme"

    version("1.64.0", commit="a8ea6b3f27e4e5bc56ff614e4549802e912db127")
    version("1.58.0", commit="257f890b64b34e6497cfde3ba694d6133805810c")

    depends_on("r-gcspikelite", type=("build", "run"))
    depends_on("r-xcms", type=("build", "run"))
    depends_on("r-camera", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-sparsem", type=("build", "run"))
