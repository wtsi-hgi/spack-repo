# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRpy2(PythonPackage):
    """rpy2 is a redesign and rewrite of rpy. It is providing a low-level
    interface to R from Python, a proposed high-level interface,
    including wrappers to graphical libraries, as well as R-like
    structures and functions.

    """

    pypi = "rpy2/rpy2-2.5.4.tar.gz"

    version("3.5.17", sha256="dbff08c30f3d79161922623858a5b3b68a3fba8ee1747d6af41bc4ba68f3d582")
    version("3.4.5", sha256="5d31a5ea43f5a59f6dec30faca87edb01fc9b8affa0beae96a99be923bd7dab3")
    version("3.3.6", sha256="ce063f3286e717b3914728ad23ec7db0a0f117ba3ade5ada8a250700779f6e77")
    version("3.2.7", sha256="db9c71eec3c91f44373839c24a1888a3999f2f342300e8e696e5dcc047d3df6d")
    version("3.1.0", sha256="ed4284df32d00b1fba5b1409e5df64b04b02d47aff543d6ef1dc211ab94e247f")
    version("3.0.4", sha256="2af5158a5d56af7f7bf5e54d8d7e87b6f115ff40f056d82f93cad0cbf6acc0cb")
    version("3.0.0", sha256="34efc2935d9015527837d6b1de29641863d184b19d39ad415d5384be8a015bce")
    version("2.9.4", sha256="be57f741d0c284b5d8785ab03dff0e829303e5ac30e548d5ceb46e05b168812e")
    version("2.8.6", sha256="004d13734a7b9a85cbc1e7a93ec87df741e28db1273ab5b0d9efaac04a9c5f98")
    version("2.5.6", sha256="d0d584c435b5ed376925a95a4525dbe87de7fa9260117e9f208029e0c919ad06")
    version("2.5.4", sha256="d521ecdd05cd0c31ab017cb63e9f63c29b524e46ec9063a920f640b5875f8a90")

    # All versions
    depends_on("py-setuptools", type="build")
    depends_on("r", type=("build", "run"))
    depends_on("py-tzlocal", type=("build", "run"))

    # @3.0.0:
    depends_on("py-cffi@1.0.0:", when="@3.0.0:", type=("build", "run"))
    depends_on("py-simplegeneric", when="@3.0.0:", type=("build", "run"))
    depends_on("py-pytest", when="@3:", type=("build", "run"))

    # @2.9.0:
    depends_on("r@3.3:", when="@2.9.0:", type=("build", "run"))
    depends_on("python@3.5:", when="@2.9.0:", type=("build", "run"))
    depends_on("py-jinja2", when="@2.9.0:", type=("build", "run"))
    depends_on("py-six", when="@2.9.0:2.9", type=("build", "run"))

    # @:2.8.6
    depends_on("r@2.8:", when="@:2.8.6", type=("build", "run"))
    depends_on("python@2.7:2.8,3.5:", type=("build", "run"))

    depends_on("zlib", type=("build", "link", "run"), when="@3.5:")
    depends_on("bzip2", type=("build", "link", "run"), when="@3.5:")
    depends_on("xz", type=("build", "link", "run"), when="@3.5:")
    depends_on("icu4c", type=("build", "link"), when="@3.5:")
    depends_on("libiconv", type=("build", "link"), when="@3.5:")
