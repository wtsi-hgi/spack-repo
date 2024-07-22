# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFilechunkio(PythonPackage):
    """FileChunkIO represents a chunk of an OS-level file containing bytes data"""

    homepage = "http://bitbucket.org/fabian/filechunkio"
    pypi = "filechunkio/filechunkio-1.8.tar.gz"

    version("1.5", sha256="882ad497d2ed6dc2cc76e6c2a0ec71ea3df5f33ce69bd87f311d6f59d023b473")
    version("1.6", sha256="163948052cd274daddfcde9cec9cb5e04ac19d7bb91606cdc6a305b0428a0e70")
    version("1.7", sha256="c30c99b6c04d28c62118bfcc94a5fecb3e7662e6b1f3d3ffe07694f05d7d7f3e")
    version("1.8", sha256="c8540c2d27e851d3a475b2e14ac109d66c777dd43ab67031891c826e82026745")

    depends_on("py-setuptools", type="build")
