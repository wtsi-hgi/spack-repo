# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrr(RPackage):
    """Rasterize Layers for 'ggplot2'.

    Rasterize only specific layers of a 'ggplot2' plot while simultaneously
    keeping all labels and text in vector format. This allows users to keep
    plots within the reasonable size limit without loosing vector properties of
    the scale-sensitive information."""

    cran = "grr"

    version("0.9.5", sha256="292606de2983ac5840c90d3e0977441b482c9e73c1674b662f8b4fb8f3632b2b")

    depends_on("r@3.0.0:", type=("build", "run"))
