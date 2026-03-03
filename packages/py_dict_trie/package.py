# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDictTrie(PythonPackage):
    """Trie implementation for approximate string matching."""

    homepage = "https://pypi.org/project/dict-trie/"
    pypi = "dict-trie/dict-trie-1.0.1.tar.gz"

    version("1.0.1", sha256="f201be32eea4a2239c1c31a0f738ad1bbb073a0bc738572606f4be5088e54ca7")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

