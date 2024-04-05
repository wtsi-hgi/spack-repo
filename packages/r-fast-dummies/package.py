# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastDummies(RPackage):
    """Fast Creation of Dummy (Binary) Columns and Rows from Categorical Variables.

    Creates dummy columns from columns that have categorical variables
    (character or factor types). You can also specify which columns to make
    dummies out of, or which columns to ignore. Also creates dummy rows from
    character, factor, and Date columns. This package provides a significant
    speed increase from creating dummy variables through model.matrix()."""

    cran = "fastDummies"

	version("1.6.3", sha256="bd3934fe19d7dff2723438bbb7b89334118143f8ce151d98477ae964ee5d81df")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
