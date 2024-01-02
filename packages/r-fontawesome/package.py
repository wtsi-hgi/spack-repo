# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RFontawesome(RPackage):
    """Easily and flexibly insert 'Font Awesome' icons into 'R Markdown' documents and 'Shiny' apps. These icons can be inserted into HTML content through inline 'SVG' tags or 'i' tags. There is also a utility function for exporting 'Font Awesome' icons as 'PNG' images for those situations where raster graphics are needed."""

    homepage = "https://github.com/rstudio/fontawesome"
    cran = "fontawesome"

    version("0.5.2", sha256="da3de2a9717084d1400d48edd783f06c66b8c910ce9c8d753d1b7d99be1c5cc9")
    version("0.5.1", sha256="f4ebbbe2ee8d2e2c0342b72095cfe668bd9800ea6c4bf7180300544bde7e566c")
    version("0.5.0", sha256="4117b417a33e82d626881d7059eb54e7534cba202e75dae7e27021cb3796e90b")
    version("0.4.0", sha256="760a0bc5b50ddbce1160b123f3b3d76342167519d75641dc2c5b952fa8d4242f")
    version("0.3.0", sha256="4deefcf4d4580d84213f863351c2a23c39adbd2f8762d7477ec2faa8235a1a31")
    version("0.2.2", sha256="572db64d1b3c9be301935e0ca7baec69f3a6e0aa802e23f1f224b3724259df64")
    version("0.2.1", sha256="65ede4b86bc8e1f958e3434035817884dc96bc62626a4f556abfd8a6b0b42469")
    version("0.2.0", sha256="d7e3cf2a163af68e8ec51e5e01eba9978fe9c4be1a3020f482000bf32d7d519c")
    version("0.1.0", sha256="c09cf09d15d53272676e9831cca360772c7a74d96818e2589efd4a7ac3fe9dbd")

    depends_on("r-rlang@1.0.6:", type=("build", "run"))
    depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))
