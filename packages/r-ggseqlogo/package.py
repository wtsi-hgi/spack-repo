# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RGgseqlogo(RPackage):
    """The extensive range of functions provided by this package makes it possible to draw highly versatile sequence logos. Features include, but not limited to, modifying colour schemes and fonts used to draw the logo, generating multiple logo plots, and aiding the visualisation with annotations. Sequence logos can easily be combined with other plots 'ggplot2' plots."""

    cran = "ggseqlogo"

    version("0.1", sha256="c14f145a982597f32264b37a5f2645206a0bee30dd2584a25cb8e3dc2f9b068f")
    version("0.0.1", sha256="cd0c00d20bffbda7a1f3efc302de9889a1a950060d288ccbce53d5814fce66e1")

    depends_on("r-ggplot2", type=("build", "run"))
