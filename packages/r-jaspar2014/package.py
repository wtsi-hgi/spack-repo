# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2014(RPackage):
    """Data package for JASPAR

    Data package for JASPAR 2014. To search this databases, please use the package TFBSTools.
    """

    homepage = "http://jaspar.genereg.net/"
    bioc = "JASPAR2014"

    version("1.44.0", commit="2b44661a379cd76514f804f7e96a699d787c31ea")
    version("1.38.0", commit="a29c998de8ac6473a56dc8c7b7aa845fd0ded4be")

    depends_on("r@3.0.1:", type=("build", "run"))
    depends_on("r-biostrings@2.29.19:", type=("build", "run"))
