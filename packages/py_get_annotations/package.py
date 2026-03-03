# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGetAnnotations(PythonPackage):
    """A backport of Python 3.10's inspect.get_annotation() function"""

    homepage = "https://github.com/shawwn/get-annotations"
    pypi = "get-annotations/get-annotations-0.1.2.tar.gz"

    version("0.1.2", sha256="da7b69b8043237cc7f7ce5919e9cc59bd18fc4e2704b43eb34e3ba4fa9374bab")
    version("0.1.1", sha256="1edc30495e34c0fd48070c6acd566ec2354ac49e30d7c55e264f61eb5692f12d")
    version("0.1.0", sha256="35d46395cdc47bc62baca383acb7a4d3e9fa892bf4108d2476951a86054ca37a")

    depends_on("py-poetry-core", type="build")
    depends_on("py-setuptools", type="build")
    depends_on("python@3.6:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import get_annotations")
