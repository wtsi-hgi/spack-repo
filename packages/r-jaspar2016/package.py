# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2016(RPackage):
    """Data package for JASPAR 2016

    Data package for JASPAR 2016. To search this databases, please use the package TFBSTools (>= 1.8.1).
    """

    homepage = "http://jaspar.genereg.net/"
    bioc = "JASPAR2016"

    version("1.36.0", commit="50f37b90e0937566af0347080277b953e8ea9409")
    version("1.30.0", commit="a363481b9aaeea5cbcb3148c448589eb93121950")

    depends_on("r@3.2.2:", type=("build", "run"))
