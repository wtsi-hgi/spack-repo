# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyFrozenlist(PythonPackage):
    """A list-like structure which implements collections.abc.MutableSequence."""

    homepage = "https://github.com/aio-libs/frozenlist"
    pypi = "frozenlist/frozenlist-1.2.0.tar.gz"

    version("1.8.0", sha256="3ede829ed8d842f6cd48fc7081d7a41001a56f1f38603f9d49bf3020d59a31ad")
    version("1.5.0", sha256="81d5af29e61b9c8348e876d442253723928dce6433e0e76cd925cd83f1b4b817")
    version("1.3.1", sha256="3a735e4211a04ccfa3f4833547acdf5d2f863bfeb01cfd3edaffbc251f15cec8")
    version("1.3.0", sha256="ce6f2ba0edb7b0c1d8976565298ad2deba6f8064d2bebb6ffce2ca896eb35b0b")
    version("1.2.0", sha256="68201be60ac56aff972dc18085800b6ee07973c49103a8aba669dee3d71079de")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("python@3.7:", when="@1.3.1:", type=("build", "run"))
    depends_on("python@:3.10", when="@:1.3.1")
    depends_on("python@:3.11", when="@:1.4.0")
    depends_on("python@:3.12", when="@:1.4.1")
    depends_on("python@:3.13", when="@:1.7")
    depends_on("python@:3.14")
    depends_on("py-setuptools@:81", type="build")
    depends_on("py-setuptools@46.4.0:", when="@1.3.1:", type="build")
    depends_on("py-expandvars", when="@1.4.1:", type="build")
    depends_on("py-setuptools@47:", when="@1.4.1:", type="build")
    depends_on("py-wheel@0.37.0:", when="@1.3.1:1.4.0", type="build")
    depends_on("py-cython", when="@1.4.1:", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import frozenlist")
