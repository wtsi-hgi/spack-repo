# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyModelcif(PythonPackage):
    """Package for handling ModelCIF mmCIF and BinaryCIF files"""

    homepage = "https://github.com/ihmwg/python-modelcif"
    pypi = "modelcif/modelcif-0.7.tar.gz"
    git = "https://github.com/ihmwg/python-modelcif"

    version("0.9", sha256="67f45ddcb9fa111be984d385167ad5cc182fc9ad5a194c523a7438dd3a140012")
    version("0.8", sha256="ea59529e0a92eed2e8a69e4513e46c1a97ceb8c2930d79e02b9d23f9fa4e525c")
    version("0.7", sha256="d6acedb2c0afb7a6964b15aa275926dd8b55c88217ae82279a1667f33f6316de")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.9", type=("build", "run"))

    depends_on("py-ihm", type=("build", "run"))
