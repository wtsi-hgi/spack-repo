# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class RScclrr(RPackage):
    """Sparse PFlog normalization and PCA for Seurat objects.

    Provides R bindings for shifted centered log-ratio normalization (PFlog) and
    sparse PCA so Seurat workflows can avoid materializing dense normalized
    matrices."""

    homepage = "https://cleartools.github.io/scclrR/"
    git = "https://github.com/cleartools/scclrR.git"

    license("BSD-2-Clause")

    version("20260619", commit="6d6378dd41502a8606da14adb01a01032cb75224")

    resource(
        name="runorm",
        git="https://github.com/cleartools/runorm.git",
        commit="9429aa00784a972fdeae64e0ca050ea08f3c5bc9",
        placement="runorm-src",
    )

    resource(
        name="ruanndata",
        git="https://github.com/pachterlab/ruanndata.git",
        commit="88a46860a59c9affb7b5605c6a267e2cfe01300d",
        placement="ruanndata-src",
    )

    resource(
        name="rupca",
        git="https://github.com/pachterlab/rupca.git",
        commit="b804cce9ba2afc78cefbcef66ffd096ffc85ed79",
        placement="rupca-src",
    )

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("rust", type="build")

    @run_after("install")
    def install_test(self):
        rscript = Executable(join_path(self.spec["r"].prefix.bin, "Rscript"))
        rscript("-e", 'library("scclrR")')
