# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScthiData(RPackage):
    """The package contains examples of single cell data used in vignettes and examples of the scTHI package; data contain both tumor cells and immune cells from public dataset of glioma

    Data for the vignette and tutorial of the package scTHI.
    """

    bioc = "scTHI.data"

    version("1.20.0", commit="9e16ff05d724d4ade702df2314966a61479ca459")
    version("1.14.0", commit="b66b93fdc141b8e3d6cc5dafbe6ec832c982ac2b")

    depends_on("r@4:", type=("build", "run"))
