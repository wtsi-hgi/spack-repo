# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassir(RPackage):
    """massiR: MicroArray Sample Sex Identifier

    Predicts the sex of samples in gene expression microarray datasets
    """

    bioc = "massiR"

    version("1.44.0", commit="5b95c70d6729227e0dc2645998807c5ee0d1ffd0")
    version("1.38.0", commit="15dce6ec955da6251efd89a88cfb4f458b524a8b")

    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-diptest", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r@3.0.2:", type=("build", "run"))
