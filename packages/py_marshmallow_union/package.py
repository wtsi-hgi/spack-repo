# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMarshmallowUnion(PythonPackage):
    """Union fields for marshmallow."""

    homepage = "https://github.com/adamboche/python-marshmallow-union"
    pypi = "marshmallow-union/marshmallow-union-0.1.15.post1.tar.gz"

    version("0.1.15.post1", sha256="c08f0a87891ae73dd2b5d4a154bc7daea20c3bc0f99ca0b6a26570c927d20c8c")

    depends_on("py-setuptools", type="build")

    depends_on("py-marshmallow@3.2.1:", type=("build", "run"))
