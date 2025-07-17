# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgabiolinksguiData(RPackage):
    """Data for the TCGAbiolinksGUI package

    Supporting data for the TCGAbiolinksGUI package.
    """

    homepage = "https://github.com/BioinformaticsFMRP/TCGAbiolinksGUI.data"
    bioc = "TCGAbiolinksGUI.data"

    version("1.28.0", commit="487076b31481187a8518c74fc36c853f42c675bd")
    version("1.22.0", commit="c3631f00ce5e737c22562f8e341c01f86f377660")

    depends_on("r@3.5:", type=("build", "run"))
