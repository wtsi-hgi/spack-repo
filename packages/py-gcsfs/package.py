# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGcsfs(PythonPackage):
    """Pythonic file-system for Google Cloud Storage."""

    homepage = "https://github.com/fsspec/gcsfs"
    pypi = "gcsfs/gcsfs-2023.1.0.tar.gz"

    license("BSD-3-Clause")

    # gcsfs.cli requires the optional fusepy/click dependencies
    skip_modules = ["gcsfs.cli"]

    version("2024.2.0", sha256="f7cffd7cae2fb50c56ef883f8aef9792be045b5059f06c1902c3a6151509f506")
    version("2023.1.0", sha256="0a7b7ca8c1affa126a14ba35d7b7dff81c49e2aaceedda9732c7f159a4837a26")

    # The bundled versioneer 0.18 uses configparser.SafeConfigParser/readfp,
    # which were removed in Python 3.12.
    conflicts("^python@3.12:", when="@:2023.1.0", msg="versioneer 0.18 is incompatible with Python 3.12+")

    depends_on("py-setuptools", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-aiohttp")
        depends_on("py-decorator@4.1.3:")
        for v in ["2024.2.0", "2023.1.0"]:
            depends_on(f"py-fsspec@{v}", when=f"@{v}")
        depends_on("py-google-auth@1.2:")
        depends_on("py-google-auth-oauthlib")
        depends_on("py-google-cloud-storage")
        depends_on("py-requests")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import gcsfs")
