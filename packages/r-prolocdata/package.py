# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProlocdata(RPackage):
    """Data accompanying the pRoloc package

    Mass-spectrometry based spatial proteomics data sets and protein complex separation data. Also contains the time course expression experiment from Mulvey et al. 2015.
    """

    homepage = "https://github.com/lgatto/pRolocdata"
    bioc = "pRolocdata"

    version("1.46.0", commit="e326d80ea4b4ec0299c4108f7384f587f005be74")
    version("1.40.0", commit="f562738194830c57f978cb36a97b09e0c6868130")

    depends_on("r@3.6.3:", type=("build", "run"))
    depends_on("r-msnbase", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
