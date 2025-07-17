# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPics(RPackage):
    """Probabilistic inference of ChIP-seq

    Probabilistic inference of ChIP-Seq using an empirical Bayes mixture model approach.
    """

    homepage = "https://github.com/SRenan/PICS"
    bioc = "PICS"

    version("2.52.0", commit="604d4b852085b6587a8aecd82d592aef9a450552")
    version("2.46.0", commit="1638a3ecc20c421e29c3ff2684c8b0ec202f1246")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("gsl", type=("build", "link", "run"))
