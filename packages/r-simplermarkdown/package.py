# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSimplermarkdown(RPackage):
    """Runs R-code present in a pandoc markdown file and includes the resulting output in the resulting markdown file."""

    homepage = "https://github.com/djvanderlaan/simplermarkdown"
    cran = "simplermarkdown"

    version("0.0.6", sha256="06d0b05455623737c1187524c864c29b70d381079b084827c40c370db3e6ce51")
    version("0.0.4", sha256="cf18612e132e2ca42b975cb4f00d3f6f549f2afec57a1a84c22d0b514b7f3719")
    version("0.0.3", sha256="847b8ac8e18f45a7b596a12bb60512ffba8c5dd5698960c321bf3ddc9de9e098")
    version("0.0.2", sha256="dcd8517aea61a558a33e3333aa5434d903abdcad0c3c1107819b20b0821399da")

    depends_on("r-rjson", type=("build", "run"))
