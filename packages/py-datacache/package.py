# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDatacache(PythonPackage):
    """Utility helpers for downloading and caching datasets."""

    homepage = "https://github.com/openvax/datacache"
    pypi = "datacache/datacache-1.4.1.tar.gz"

    version("1.4.1", sha256="acfdbdc550c7e0971b42ec0575cec2245ec4ace1cdfb9e931852db157e5b6c67")

    depends_on("py-setuptools", type="build")
    depends_on("py-pandas@0.15.2:", type=("build", "run"))
    depends_on("py-appdirs@1.4.0:", type=("build", "run"))
    depends_on("py-progressbar33@2.4:", type=("build", "run"))
    depends_on("py-requests@2.5.1:", type=("build", "run"))
    depends_on("py-typechecks@0.0.2:", type=("build", "run"))
    depends_on("py-mock", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import datacache")
