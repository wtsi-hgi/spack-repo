# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMoodsPython(PythonPackage):
    """MOODS: Motif Occurrence Detection Suite"""

    homepage = "https://www.cs.helsinki.fi/group/pssmfind/"
    pypi = "MOODS-python/MOODS-python-1.9.4.1.tar.gz"

    version("1.9.3", sha256="6022878918e82e84c3d764d2f725bbb56b41942565e7595c478bb40f02ff8b14")
    version("1.9.3.1", sha256="4deec2c3b872a549be462612f98a9956ae376b8f4949fcb0f276dcd2da6ac596")
    version("1.9.4.1", sha256="b3b5e080cb0cd13c0fd175d0ee0d453fde3e42794fa7ac39a4f6db1ac5ddb4cc")

    depends_on("py-setuptools", type=("build"))
