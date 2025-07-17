# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformeasure(RPackage):
    """R implementation of information measurements

    This package consolidates a comprehensive set of information measurements, encompassing mutual information, conditional mutual information, interaction information, partial information decomposition, and part mutual information.
    """

    homepage = "https://github.com/chupan1218/Informeasure"
    bioc = "Informeasure"

    version("1.18.0", commit="7df4c919c3e1b0f4d8f95fdb7798a1736c244880")
    version("1.12.1", commit="7e10f65378e90f8698e9922ee6dff080fe0af9e7")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-entropy", type=("build", "run"))
