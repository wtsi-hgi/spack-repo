# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactr(RPackage):
    """Make it easy to use 'React' in R with 'htmlwidget' scaffolds, helper dependency functions, an embedded 'Babel' 'transpiler', and examples."""

    homepage = "https://github.com/react-R/reactR"
    cran = "reactR"

    version("0.4.4", sha256="5cb88fb365a986cba36c99c26f6c96692c5fa85fd3be7fe7564dd3d7878c8095")
    version("0.4.3", sha256="5ccce7c73fa0f6b22154e07646e11c559e6fbe04da50d2fe1fd8dcbfdff69873")
    version("0.4.2", sha256="c50503b1e4ef49d2a75a1305ba49fd3543da0a123e1e8d292c19403675872a87")
    version("0.4.1", sha256="bb734160c17b6df8e857a50e97b36e3a35b2c734e3c71e507bc60c9d3c06fd3b")
    version("0.4.0", sha256="cdd648429b07719996646e336078b3e58fb9969e5bf077c098c1a119af668bbb")
    version("0.3.0", sha256="e93e2d42989b7bf4acab86488249537981604e9c91e1654f7dc41c5a46fc9dff")
    version("0.2.1", sha256="063dd0c011d95c98be35085ebbfde95a4851bd466b0bfb4ab497cc2d201d72a9")
    version("0.2.0", sha256="b8947246db2145ca89fac01389f12efe9a7035b6945255e350aebb92fc624d9e")
    version("0.1.4", sha256="579d623ad2b60ea90f4d4af582871e28577b84c17e87e08b7dbb2a9f22683d8a")
    version("0.1.3", sha256="a584c440f0b57ad9f331926529eb9e8cd600462d231b4cb2612c8af4a2543c53")
    version("0.1.2", sha256="cf56ea00d2b495628bf1d687988f094f8abc16db18c8c3b0a40063711c522f04")
    version("0.1.0", sha256="668bb1c0e3bf01699949844137acbd67d337d80d08616802c974852162cb86bb")

    depends_on("r-htmltools", type=("build", "run"))
