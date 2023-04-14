# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTyper(PythonPackage):
    """Typer, build great CLIs. Easy to code. Based on Python type hints.

    Typer is a library for building CLI applications that users will love using
    and developers will love creating. Based on Python 3.6+ type hints."""

    homepage = "https://typer.tiangolo.com"
    pypi = "typer/typer-0.7.0.tar.gz"

    version("0.7.0", sha256="ff797846578a9f2a201b53442aedeb543319466870fbe1c701eab66dd7681165")

    depends_on("py-flit-core", type="build")
    depends_on("py-click", type=("build", "run"))
