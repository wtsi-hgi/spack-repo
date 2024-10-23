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
#     spack install r-hdpx
#
# You can edit this file again by typing:
#
#     spack edit r-hdpx
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RHdpx(RPackage):
    """R pkg for hierarchical Dirichlet process mixture modeling."""

    homepage = "https://github.com/steverozen/hdpx"
    url = "https://github.com/steverozen/hdpx/archive/refs/tags/v1.0.5-bis.tar.gz"

    license("GPL-3.0")

    version(
        "1.0.5-bis",
        sha256="8118cc20ff60de5374d5ee61fa21e308e2796d363ba7e2963b37b4430ab1de2e",
    )
    version(
        "1.0.5",
        sha256="922c61759d337e61cfeae717882871734a047826032c4619778caa430d27dab8",
    )
    version(
        "1.0.1",
        sha256="559c01f09134f54518d3c9a8847aa182eb269cb061d832ee0fb98ca1dc2c0840",
    )
    version(
        "0.3.9",
        sha256="18f2ce67636cc52c0d90cd010844a6bea8430f840c2c9e5f5c0cec99d2fdf77d",
    )
    version(
        "0.3.8",
        sha256="c0a5ceb2951a3dbadfa6ffa9f67af9285fa24b3db18e961479af50f3a2f44f9b",
    )
    version(
        "0.3.4",
        sha256="d61ed4d028db1ddb02a26e0dcc4aff8295e800886bda1703fe7a5926a0d61103",
    )
    version(
        "0.3.2",
        sha256="016fb425a3bea564d91d21f6426d826a060ddfc02c501cda3d62ab963801813e",
    )
    version(
        "0.3.0",
        sha256="9c7a4bb0dc9bf40a48937c1548488f417ed3831d808fe536410fb1f72ddf4bdb",
    )
    version(
        "0.1.7",
        sha256="ba2322b3bbd6b0c9b48dfc6c397af5c4ee86785f310692c29199af3268333858",
    )

    depends_on("r-lsa", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-dendextend", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-icams", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-beeswarm", type=("build", "run"))
    depends_on("r-paralleldist", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
