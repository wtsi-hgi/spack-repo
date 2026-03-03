# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyreadr(PythonPackage):
    """A python package to read and write R RData and Rds files into/from pandas dataframes. It does not need to have R or other external dependencies installed."""

    homepage = "https://github.com/ofajardo/pyreadr"
    pypi = "pyreadr/pyreadr-0.5.3.tar.gz"

    version("0.5.3", sha256="71517866240ed195e7933ed9c47129e738d6f23c3269556f1db4037554ecf455")
    version("0.5.2", sha256="33d5747fe210d41e4a329afef2232c9d1258847094b87a2a96efffbef223fae8")
    version("0.5.1", sha256="cc3b9d27d6a9aa8984ea973544fd922caea237067620dd68147163b6746590b6")
    version("0.5.0", sha256="7fb9f8c4afb5aac1e5bf8175bf295bc4f421eb33ba7c093f455d077f91fe73c0")
    version("0.4.9", sha256="448440079ee5be06bc03192f691314c55c9f94bc4e06c44da166a7baa56c2602")
    version("0.4.8", sha256="95f677019567b86d49e3f60c6c67edd1f8d2afe7f2aac3b419d90c98bfa42890")
    version("0.4.7", sha256="901110d62b4bedaef288f4db81425fb696edc721fe2c34c1083f5fb11050a73c")
    version("0.4.6", sha256="681bc7500628725a483b6d535918e779e606d8a43f3a9ed09a9eb117e02a0f03")
    version("0.4.5", sha256="d2981c10be4266d852f65b75f5be0527212c0979e4d6c376eaa987674cedf406")
    version("0.4.4", sha256="690a6d87f25b6b211bad0d73fe0c9be87718e62329b142d835eadd951982c6ad")

    depends_on("python@3.6:", type=("build", "run"))

    depends_on("bzip2")
    depends_on("xz")
    depends_on("zlib")
    depends_on("py-setuptools", type="build")
    depends_on("py-pandas@0.24.2:", type=("build", "run"))
    depends_on("py-cython@3.0.0:", type="build", when="@0.5.0:")
    depends_on("py-cython@0.29.36", type="build", when="@:0.4.99")
    depends_on("py-wheel", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    def setup_build_environment(self, env):
        for dep in ("bzip2", "xz", "zlib"):
            headers = self.spec[dep].headers
            libs = self.spec[dep].libs
            if headers:
                env.append_flags("CPPFLAGS", headers.cpp_flags)
            if libs:
                env.append_flags("LDFLAGS", libs.ld_flags)
