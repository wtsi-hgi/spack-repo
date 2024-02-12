# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPlumbum(PythonPackage):
    """Ever wished the compactness of shell scripts be put into a real programming language? Say hello to Plumbum Shell Combinators. Plumbum (Latin for lead, which was used to create pipes back in the day) is a small yet feature-rich library for shell script-like programs in Python. The motto of the library is “Never write shell scripts again”, and thus it attempts to mimic the shell syntax (“shell combinators”) where it makes sense, while keeping it all Pythonic and cross-platform."""

    homepage = "https://github.com/tomerfiliba/plumbum"
    pypi = "plumbum/plumbum-1.8.2.tar.gz"

    version("1.8.2", sha256="9e6dc032f4af952665f32f3206567bc23b7858b1413611afe603a3f8ad9bfd75")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

