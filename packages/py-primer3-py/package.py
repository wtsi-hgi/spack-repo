# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrimer3Py(PythonPackage):
    """Primer3-py is a Python-abstracted API for the popular Primer3 library. The intention is to provide a simple and reliable interface for automated oligo analysis and design."""

    homepage = "https://github.com/libnano/primer3-py"
    url = "https://github.com/libnano/primer3-py/archive/refs/tags/v2.0.3.tar.gz"

    version("2.0.3", sha256="2d63fe72553fd9db5cd01b40c5c68fa0cf672e4ac03571ea2a9759145e270d1e")
    version("2.0.2", sha256="459a1dc5ba57602dc55ec6ce439a3967e6c527ccf047cc0df7f93061cb2ca2af")
    version("2.0.1", sha256="9263d7494ed07c7054e6b6084e65cfb6c21c37a523b10925e374481dd9209ac1")
    version("2.0.0", sha256="5546f8bff6359937f7bbd8dcd375bcd269e02ce6ed56cddfcbe88d8b5b5b3692")
    version("1.2.2", sha256="809c89e07ca17ec1e06fad3236ee64426414083eb930c7961d0df5906c1d4da8")
    version("1.2.1", sha256="f304eb51ec175de4ab01890e6eba8e70722c366eec260e11909a932befc21fdc")
    version("1.2.0", sha256="7caff275a72a499e4f582bb542456996345323f7800af75bea2f87723036a5a8")
    version("1.1.0", sha256="18d7d18d31d28ebd49a26bc747cb0d23d4834cce9896d256afece4d2da17ebca")
    version("1.0.0", sha256="c9e86f83bfd647cdc4b83a6a931ccec08ef374e3560cbf38fed42caa3825e65e")

    depends_on("python@3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("primer3", type=("build", "run"))
