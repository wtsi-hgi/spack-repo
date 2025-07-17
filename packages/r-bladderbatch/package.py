# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBladderbatch(RPackage):
    """Bladder gene expression data illustrating batch effects

    This package contains microarray gene expression data on 57 bladder samples from 5 batches. The data are used as an illustrative example for the sva package.
    """

    bioc = "bladderbatch"

    version("1.46.0", commit="4545572d00e852e1cd33c71c71e511e3e12b561e")
    version("1.40.0", commit="ac1635f99901b02a8c832fe98facb0a687845196")

    depends_on("r-biobase", type=("build", "run"))
