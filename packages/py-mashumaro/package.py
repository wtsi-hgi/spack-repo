# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMashumaro(PythonPackage):
    """Fast and well tested serialization library for Python"""
    
    homepage = "https://github.com/Fatal1ty/mashumaro"
    pypi = "mashumaro/mashumaro-3.14-py3-none-any.whl"

    version("3.14", sha256="c12a649599a8f7b1a0b35d18f12e678423c3066189f7bc7bd8dd431c5c8132c3", expand=False, url="https://files.pythonhosted.org/packages/1b/35/8d63733a2c12149d0c7663c29bf626bdbeea5f0ff963afe58a42b4810981/mashumaro-3.14-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-typing-extensions", type=("build", "run"))