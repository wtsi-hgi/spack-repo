# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPyspoa(PythonPackage):
    """Python bindings to spoa"""

    homepage = "https://github.com/nanoporetech/pyspoa"
    pypi = "pyspoa/pyspoa-0.0.8.tar.gz"

    license("MIT")

    version("0.2.1", sha256="a8a7b7df3faa1b5bb16d6b4e82099b1c9aca604c8288bcf8ca4960d376f7ff8c")
    version("0.2.0", sha256="714f236d70f663f3b6550adca6029028a5ed620588459a95fd74044df256f8cf")
    version("0.1.0", sha256="766afef72fa39609432c2a891e9d535728de4a649656c95a66295d0d61133e5d")

    # depends_on("c", type="build")  # generated
    # depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("cmake@3:", type="build")
    depends_on("zlib-api")

    depends_on("py-pybind11@2.4:", type=("build", "run"))
