# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViper(RPackage):
    """Virtual Inference of Protein-activity by Enriched Regulon analysis

    Inference of protein activity from gene expression data, including the VIPER and msVIPER algorithms
    """

    bioc = "viper"

    version("1.42.0", commit="341d73132e43184c93816302a9ee12f2433e9d69")
    version("1.36.0", commit="5cf7edbfb21a516dcce2aa8c5a4a58ecf8fcdc79")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
