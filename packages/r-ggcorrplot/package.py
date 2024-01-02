# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-ggcorrplot
#
# You can edit this file again by typing:
#
#     spack edit r-ggcorrplot
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RGgcorrplot(RPackage):
    """The 'ggcorrplot' package can be used to visualize easily a correlation matrix using 'ggplot2'."""

    homepage = "http://www.sthda.com/english/wiki/ggcorrplot-visualization-of-a-correlation-matrix-using-ggplot2"
    cran = "ggcorrplot"

    version("0.1.4.1", sha256="b810950cff07e95865ddd042ad060a40e66414b69fc604b1242410ed6831a879")
    version("0.1.4", sha256="59829e17f6cf5ad49201c8b981e83615dfd75ea0a2b4251d11f7c6db6e05caa0")
    version("0.1.3", sha256="2b9085b72b14e616edb3cda43159dfcb68675ea7389fbaa8a041f920c2a72942")
    version("0.1.2", sha256="23c192c8c8e074d5835fe00196ce5d80f4b37990eed432e6ba5f3f3953db5d8b")
    version("0.1.1", sha256="a1c0b3230e0893b261b53ffdcce56c0afc4dd41640854be37d0bf9a72f0e5812")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
