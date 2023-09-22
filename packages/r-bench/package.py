# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBench(RPackage):
    """High Precision Timing of R Expressions
    
    Tools to accurately benchmark and analyze execution times for R expressions.
    """

    homepage = "https://bench.r-lib.org/"
    cran = "bench"

    version("1.1.3", sha256="bfae6320ad8c0c84fa6832519fac0e783e8d3ac5e3019ff6526f8060e8f1f317")

    depends_on("r-glue", type=("build", "run"))
    depends_on("r-pillar", type=("build", "run"))
    depends_on("r-profmem", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
