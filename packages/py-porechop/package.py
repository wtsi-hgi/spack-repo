# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPorechop(PythonPackage):
    """Nanopore adapter trimmer and demultiplexer with a bundled C++ backend."""

    homepage = "https://github.com/rrwick/Porechop"
    url = "https://github.com/rrwick/Porechop/archive/refs/tags/v0.2.4.tar.gz"

    license("GPL-3.0-or-later")

    version("0.2.4", sha256="44b499157d933be43f702cec198d1d693dcb9276e3c545669be63c2612493299")
    version("0.2.3", sha256="bfed39f82abc54f44fffd9b13d2121868084da7ac3d158ac9b9aa6fa0257f0f4")
    version("0.2.2", sha256="5cb373bd6a95ec9c7003c3c01501aafaf2ca3bc27fa843a016510ed88eecec93")
    version("0.2.1", sha256="e5259d29e15eace012f909a07ee2eff80e104890b2e96f9c03bf89b744a77935")
    version("0.2.0", sha256="b3af5e271956fb84bc2918a3c2d7cbe8e4f0f4fcd40542db8d689c9489adaae6")
    version("0.1.0", sha256="f393be9ba32a9f0dc8dd3b2262c9b0f839e364b26f37698d7ef485ed0d9e72fd")

    depends_on("py-setuptools", type="build")

    def setup_build_environment(self, env):
        env.set("CXX", self.compiler.cxx)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            porechop = Executable(join_path(self.prefix.bin, "porechop"))
            porechop("--version")
