# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactable(RPackage):
    """Interactive data tables for R, based on the 'React Table' JavaScript library."""

    homepage = "https://glin.github.io/reactable/"
    cran = "reactable"

    version("0.4.4", sha256="b4aae6be2dd85aaa5226067415e501abc139e99499bc62c539630eeafdaf6af2")
    version("0.4.3", sha256="97fd4bc79ddbf22f1ac5ddaf6aae8d32cc3ac953b0446fdb5140cda319c3feec")
    version("0.4.2", sha256="80448ab11af6b721e8b20d88c7c55421463ec63e0bd930b73d626824d1bfa157")
    version("0.4.1", sha256="b380768af7b34d019dc1ea522f1c2b21023b8fdcd9b28cad028773c332ed9dcd")
    version("0.4.0", sha256="13b15ed4307a1f80ad8b4ad1639c1c92d85b7f7ce383ead9367e5c05d9bf7c26")
    version("0.3.0", sha256="38e4d49a235f6900e6d7dcb33245c925860edf0b3eb443c78ee0330b6a0c304d")
    version("0.2.3", sha256="fd665a5d8d0c86cf98bb57fea0f5d795adca8fdc2651c8067e1954ba5839949f")
    version("0.2.2", sha256="850bd9b608861a030a435246e88836eb659fcfbdbb397eb26f370200f4983421")
    version("0.2.1", sha256="f7dd1d978a4d8f9e4eaa79383a40134f94762931d9b3bdbb81b0111b45d563de")
    version("0.2.0", sha256="e2fca12435967f58ddc87127ac5034710ec2bf2411ab63752ceaa69cd41fed0c")
    version("0.1.0.1", sha256="a3da740a2ca9e2c3d9374b3b2473393e996bcdcf79d12532b38bbe695ba0a95d")
    version("0.1.0", sha256="8daccfab51f8dbb1a157c9e798c5c8c2d89b5a1ba9dc693906441df150d7cd03")

    depends_on("r-digest", type=("build", "run"))
    depends_on("r-htmltools@0.5.2:", type=("build", "run"))
    depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-reactr", type=("build", "run"))
