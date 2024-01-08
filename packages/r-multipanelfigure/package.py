# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RMultipanelfigure(RPackage):
    """Tools to create a layout for figures made of multiple panels, and to fill the panels with base, 'lattice', 'ggplot2' and 'ComplexHeatmap' plots, grobs, as well as content from all image formats supported by 'ImageMagick' (accessed through 'magick')."""

    cran = "multipanelfigure"

    version("2.1.5", sha256="e2a8ccfe5750197a6c0e4bf9f53e18a4fd43446446d36cdf40b6cf442e1ec2cb")
    version("2.1.2", sha256="eca98888d2f7c8887764443633bd557e9100f73694b2e5df68a63b304f5ba532")
    version("2.1.1", sha256="e0ba8a6b428ea2acdc129d4bd615eb83069edc767f966f5548cdc54758ecfeef")
    version("2.0.2", sha256="47b04774f10ce11d57298af76b7e2e7c27545ccfa815131b63c99bae2b584438")
    version("2.0.0", sha256="2afc889ac5fb5fab90e37a0569cfe57fb5cca15f02000d4a6b2e3b3cf98d2d5d")
    version("1.1.2", sha256="f347a61367f75f518219a623507f34347edee478d6813739b4bf4f798bc81532")
    version("1.0.0", sha256="faadf5ca4dfc1f1975bb7df2bc9bf1679a6166fcbfc2fe5b58cbf337daf87c23")
    version("0.10.7", sha256="30101de914811f69b0a17e2866215535a6eef9fa7693a1c437dffb559594f71c")
    version("0.10.6", sha256="037a447bbcdce331fb0a2fa69f4857e505ef1136b9bfea831b6a79bbac72a3ec")
    version("0.10.5", sha256="f678b96011e13b3685116d85d0eea413445ec1b97d1458a9793b2f5e51dca42a")
    version("0.10.3", sha256="55ad8f7a6c199a02f63562dc6ec9879e2cff82e513c1ed30ea4a0ca7814b86e7")
    version("0.9.0", sha256="a3fd043af3495edf5b4b3b3032e0765eb250aeae5a78b67aecfd045482e574ed")
    version("0.8.3", sha256="90cceaa63e76a6b91511bc0dd3929b996b5e3c95b6c0b51c25ab434471f052d6")
    version("0.8.2", sha256="3c5aaa5a4f0c21abbaab0d8b60e11e40133a8781e13333c47fcf91977702f422")

    depends_on("r-assertive-base@0.0-7:", type=("build", "run"))
    depends_on("r-assertive-files@0.0-2:", type=("build", "run"))
    depends_on("r-assertive-numbers@0.0-2:", type=("build", "run"))
    depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
    depends_on("r-gridgraphics@0.3-0:", type=("build", "run"))
    depends_on("r-gtable@0.2.0:", type=("build", "run"))
    depends_on("r-magick@1.9:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-stringi@1.2.3:", type=("build", "run"))
