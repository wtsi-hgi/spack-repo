# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvddata(RPackage):
    """Drug versus Disease Data

    Data package which provides default drug and disease expression profiles for the DvD package.
    """

    bioc = "DvDdata"

    version("1.44.0", commit="ba2be704908627e4375b1f937774fd6d6c22ebeb")
    version("1.38.0", commit="191d798d58657fff7458d538c3eb666449ea52ee")

    depends_on("r@2.10:", type=("build", "run"))
