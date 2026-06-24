# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRdkit(PythonPackage):
    """A collection of chemoinformatics and machine-learning software written in C++ and Python"""
    
    homepage = "https://github.com/kuelumbus/rdkit-pypi"
    git = "https://github.com/kuelumbus/rdkit-pypi"

    version("2026.03.3", tag="2026.03.3")
    version("2025.09.6", tag="2025.09.6")
    version("2025.03.3", tag="2025.05.3")

    depends_on("py-setuptools@75:", type=("build"))
    depends_on("py-wheel", type=("build", "run"))
    depends_on("py-cmake@3.31:", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-conan@2.0.0:", type=("build"))
    depends_on("py-ninja", type=("build"))
    depends_on("py-pybind11-stubgen", type=("build"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("cairo", type=("build", "link", "run"))

    def patch(self):
        filter_file("to_path = Path(\"/usr/local/lib\")", "to_path = Path(\""+self.prefix+"/lib\")", "setup.py", string=True)
        filter_file("cmds.append(\"ldconfig\")", "", "setup.py", string=True)

    def setup_build_environment(self, env):
        env.set("CIBW_BUILD", f"cp{self.spec['python'].version[0]}{self.spec['python'].version[1]}-manylinux_x86_64")

#    def config_settings(self, spec, prefix):
#        return {
#            '--install-headers=': prefix.include,
#            '--install-lib=': prefix.lib,
#            '--matrix-args=-DCMAKE_INSTALL_PREFIX=':  prefix
#        }
