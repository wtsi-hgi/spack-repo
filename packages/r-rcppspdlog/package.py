# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRcppspdlog(RPackage):
    """The mature and widely-used C++ logging library 'spdlog' by Gabi Melman provides many desirable features."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/eddelbuettel/rcppspdlog"
    cran = "RcppSpdlog"

    version("0.0.14", sha256="8cb4fdf7cbaa001064b074f7339d0b3c53c13723d6bc7af6f873989cc5afc3d8")
    version("0.0.13", sha256="73dc2c33ec7a9d5b8ffa7270cc2f32a9c75cd98ce990126e86018c43009c8984")
    version("0.0.12", sha256="9db914047a5b7b5c863c059a2db83ad051168093a14e4d0315b4f5442a0456d9")
    version("0.0.11", sha256="71b1509521ae2dc4a94aefdebe3c2a49a0b037c591b5ec8cf1e1b30191e41b88")
    version("0.0.10", sha256="0ecaf0df120af510db2dc75aaaa40ae6bc1baf7f488fc8763137ff2a9f0b23a5")
    version("0.0.9", sha256="96979e75365ef19af35abe92b20f4416397ad99e120191b21b4049fbe368207a")
    version("0.0.8", sha256="ea8f7f6247ed03a544225fb35c9e7949eb27fd012adbee2c81975e9d6278aefc")
    version("0.0.7", sha256="db3e22a5e76e1b045196ed9793187a120fcd985e5eccfd6a7c1756646a43968d")
    version("0.0.6", sha256="d3a71787d79d71c0f8ffe81a517ab7acafcab6a194ba4f962050c89f8fe62be9")
    version("0.0.5", sha256="38208a1e8d0bf6110c890269db18908030804efbe1a058e1b3d7a540af857517")
    version("0.0.4", sha256="5bf7d6bb25078fa3d61252538babc7a6b8b5c589b583638ad023123b7b18180b")
    version("0.0.3", sha256="d38a8bac8941561a122afa4b3f0fd9c57681361ed0885357882e7086f1bed24b")
    version("0.0.2", sha256="a3090fa4646dd8b9f529e5b8b1d3038ebb038898ea1c59c4c32dc64ae8125854")
    version("0.0.1", sha256="30bb4497823c2b1a55258d453381f23a9f8096cc998390a2b41dddb2d8518fca")

    depends_on("r-rcpp", type=("build", "run"))
