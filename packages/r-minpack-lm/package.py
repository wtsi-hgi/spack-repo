# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinpackLm(RPackage):
    """R Interface to the Levenberg-Marquardt Nonlinear Least-Squares Algorithm Found in MINPACK"""

    homepage = "https://cran.r-project.org/web/packages/minpack.lm/index.html"

    cran = "minpack.lm"
    version("1.2-4", sha256="e30fa4fe353cf00d266839d3c5db83ec9548a660f31d447ad9a69f556d56e731")

    depends_on("r+X", type=("build", "run"))

