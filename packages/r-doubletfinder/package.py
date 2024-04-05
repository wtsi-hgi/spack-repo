# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RDoubletfinder(RPackage):
    """DoubletFinder is an R package that predicts doublets in single-cell RNA sequencing data."""

    git = "https://github.com/chris-mcginnis-ucsf/DoubletFinder"

	version("2023.-08-18", commit="1b1d4e2d7f893a3552d9f8f791ab868ee4c782e6")

    depends_on("r-fields", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))
