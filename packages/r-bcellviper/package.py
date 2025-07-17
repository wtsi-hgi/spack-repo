# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcellviper(RPackage):
    """Human B-cell transcriptional interactome and normal human B-cell expression data

    This package provides a human B-cell context-specific transcriptional regulatory network and a human normal B-cells dataset for the examples in package viper.
    """

    bioc = "bcellViper"

    version("1.44.0", commit="c5d0d288cfc39ac29075a5d915f4856c61be2ad0")
    version("1.38.0", commit="121a0fba4540a8125bc99e4b0d43cb8e7ecadbc8")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
