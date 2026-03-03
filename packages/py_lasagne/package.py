# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLasagne(PythonPackage):
    """A lightweight library to build and train neural networks in Theano"""

    homepage = "https://github.com/Lasagne/Lasagne"
    git = "https://github.com/Lasagne/Lasagne.git"
    pypi = "Lasagne/Lasagne-0.1.tar.gz"

    version("0.1.1", commit="5d3c63cb315c50b1cbd27a6bc8664b406f34dd99")  # unofficial version from master branch
    version("0.1", sha256="3c634ecab67e43e4f18520932bfd88bd3c678ec723c48177f18799dab2411233")

    depends_on("py-theano", type=("build", "run"))
