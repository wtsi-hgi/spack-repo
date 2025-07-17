# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlpe(RPackage):
    """Local Pooled Error Test for Differential Expression with Paired High-throughput Data

    This package performs tests for paired high-throughput data.
    """

    homepage = "http://www.korea.ac.kr/~stat2242/"
    bioc = "PLPE"

    version("1.68.0", commit="5db6e6e3029096913e5db34bfd8931b2289340e7")
    version("1.62.0", commit="19a299c6e6da9ef7cd4a4a02db78158dfd720bf3")

    depends_on("r@2.6.2:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-lpe", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
