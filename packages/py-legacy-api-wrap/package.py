# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLegacyApiWrap(PythonPackage):
    """Wrap legacy APIs in Python projects."""

    homepage = "https://github.com/flying-sheep/legacy-api-wrap"
    pypi = "legacy-api-wrap/legacy_api_wrap-1.5.tar.gz"

    license("MPL-2.0")

    version("1.5", sha256="b41ba6532f3ebfe3a897a35a7f97dec3be04b92a450f6c2bcf89f1b91c9cadf2")
    version("1.4.1", sha256="9c40d67aa8312fec8763e87cbf28fea4b67710c79ca7a18137b573d150f3b2b4")
    version("1.4", sha256="92dfa274cedb26d6e6f70fac85c856fbdcc05058066656d76a665fb4bf11b785")
    version("1.3", sha256="175b7b8af157eedb5b3dbc941e2fbff7cc9da2880382cbb8ea3a01c73404b81e")
    version("1.2", sha256="034a44612da7e9943d3964363a98937ab54d55e3301075374abe0d521eb8101b")
    version("1.1", sha256="8a6caef826d781d84d80ac61dc06bad826c965386aa1319fde41b831eca998b6")
    version("1.0", sha256="dcc2cf5440bd321523514c050a3bca152e3686ebd6919be98dd27eda6aef1ca8")
    version("0.1", sha256="273d96e83317bae4495b2fcf12f2594dea3ccbc3d45cfdca3e6d056551380aac")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatch-docstring-description", type="build")
    depends_on("py-hatch-vcs", type="build")
    depends_on("py-hatchling", type="build")

    def patch(self):
        filter_file(
            '  "Programming Language :: Python :: 3.14",\n',
            "",
            "pyproject.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import legacy_api_wrap")
