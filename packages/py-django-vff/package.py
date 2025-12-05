# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDjangoVff(PythonPackage):
    """Versioned file field with Git-backed history for Django models."""

    homepage = "https://github.com/Yaco-Sistemas/django-vff"
    pypi = "django-vff/django-vff-0.2b3.tar.gz"

    version("0.1a1dev", sha256="a85f5605b7a9d9ff483df23601cf15eb7e3fc78ffe3d718b85d7d9539f2fbcdf")
    version("0.1b1", sha256="9900abfb07d8590d7e8d3c8d83e1c38acf8390bc6499fb201505151eb65e42b9")
    version("0.1b2", sha256="2218bb686e6bdf70dd7cfccb2b965cf7bc181a55772ccea3230f394006d13267")
    version("0.1b3", sha256="b142a912362481c4068e0250073461d7085ccc4907c25ad518ed2ca36c77266a")
    version("0.1b4", sha256="6fff07381c490896ed6e834cf3cb446d63d7215581e2b8114fe265d0c76710cc")
    version("0.2b1", sha256="cdd190cb5b8ce62f7cd5fc262ed46958a816ab2afc0f7ed276cf588ba8d7e761")
    version("0.2b2", sha256="480d22861fbe96ca29ffc0a375269acf55b013184c0f85388ddbee19c5cf3dad")
    version("0.2b3", sha256="0930a9c9dae2b88db6df84d2798a7fe0dce549c49fe6387a5b45fa3bcef695b2")

    depends_on("py-setuptools", type="build")
    depends_on("py-django", type=("build", "run"))
    depends_on("py-gitpython@3:", type=("build", "run"))

    def patch(self):
        filter_file(
            "'GitPython==0.3.6'",
            "'GitPython>=0.3.6'",
            "setup.py",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import vff")
