# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupradar(RPackage):
    """Assessment of duplication rates in RNA-Seq datasets

    Duplication rate quality control for RNA-Seq datasets.
    """

    homepage = "https://www.bioconductor.org/packages/dupRadar"
    bioc = "dupRadar"

    version("1.38.0", commit="a0df46842d4da8be8d4d8bbac65c0e310dd96d12")
    version("1.32.0", commit="7e07fc3a3901f8cae0203759fc24dd7df430a07f")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rsubread@1.14.1:", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
