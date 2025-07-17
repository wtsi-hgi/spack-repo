# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBufferedmatrixmethods(RPackage):
    """Microarray Data related methods that utlize BufferedMatrix objects

    Microarray analysis methods that use BufferedMatrix objects
    """

    homepage = "https://github.bom/bmbolstad/BufferedMatrixMethods"
    bioc = "BufferedMatrixMethods"

    version("1.72.0", commit="62ad483cd00aae3b9b2ef5da19ee58e3e9e4f1cd")
    version("1.66.0", commit="be08e2eac4147aea3d8206fc85f0f29cff795738")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-bufferedmatrix", type=("build", "run"))
