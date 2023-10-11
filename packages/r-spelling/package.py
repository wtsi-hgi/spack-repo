# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RSpelling(RPackage):
    """Spell checking common document formats including latex, markdown, manual pages, and description files."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://docs.ropensci.org/spelling/"
    cran = "spelling"

    version("2.2.1", sha256="4fd4afcb5caa010630372c2dd32c34e8fc02ae385425c1f4b7dae697f8ab256f")
    version("2.2", sha256="740dc8546d096f89d796d8778d522ae980fbde6e0d105170c2f8881d7892369d")
    version("2.1", sha256="570e3803a7cc97dc43068fed16cad842794044afb00f71426c43fd24705e22c9")
    version("2.0", sha256="c1a209aafd603d6429538a2433a4d0ad467a5c79aac473a7d843c59b11d12fa5")
    version("1.2", sha256="448772eccd4b7bfd8788a7a8064140cab92ff666134cdc512be00b0b3eefbdbd")
    version("1.1", sha256="d1220abbd192195a9933243cf93d7f0b31717bd18f4b1fc99bb470e9effaf083")
    version("1.0", sha256="590a6d4e84748504dc87fc5a1698a66ad4a4cd54cf17e78dee0eac50081d4964")

    depends_on("r-commonmark", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-hunspell@3.0:", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
