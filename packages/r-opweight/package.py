# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpweight(RPackage):
    """Optimal p-value weighting with independent information

    This package perform weighted-pvalue based multiple hypothesis test and provides corresponding information such as ranking probability, weight, significant tests, etc . To conduct this testing procedure, the testing method apply a probabilistic relationship between the test rank and the corresponding test effect size.
    """

    homepage = "https://github.com/mshasan/OPWeight"
    bioc = "OPWeight"

    version("1.30.0", commit="635986d42da38f5781687ea28c4b18f7c9d145b7")
    version("1.24.0", commit="d777e9dc96a0a49a573c4562a49768e32bc6a876")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
