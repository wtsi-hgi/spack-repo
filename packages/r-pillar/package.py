# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPillar(RPackage):
    """Coloured Formatting for Columns.

    Provides a 'pillar' generic designed for formatting columns of data using
    the full range of colours provided by modern terminals."""

    cran = "pillar"

    version("1.9.0", sha256="f23eb486c087f864c2b4072d5cba01d5bebf2f554118bcba6886d8dbceb87acc")

    depends_on("r-cli", type=("build", "run"))
    depends_on("r-cli@2.3.0:", type=("build", "run"), when="@1.7.0:")
    depends_on("r-fansi", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"), when="@1.6.5:")
    depends_on("r-lifecycle", type=("build", "run"), when="@1.4.7:")
    depends_on("r-rlang@0.3.0:", type=("build", "run"))
    depends_on("r-rlang@1.0.2:", type=("build", "run"), when="@1.8.1:")
    depends_on("r-utf8@1.1.0:", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"), when="@1.4.0:")
    depends_on("r-vctrs@0.2.0:", type=("build", "run"), when="@1.4.7:")
    depends_on("r-vctrs@0.3.8:", type=("build", "run"), when="@1.6.1:")
    depends_on("r-crayon@1.3.4:", type=("build", "run"))
    depends_on("r-crayon", when="@:1.7.0")
    depends_on("r-ellipsis", type=("build", "run"), when="@1.4.7:")
    depends_on("r-ellipsis@0.3.2", type=("build", "run"), when="@1.6.1:")
    depends_on("r-ellipsis", when="@:1.7.0")
