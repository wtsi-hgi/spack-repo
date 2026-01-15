# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTriqler(PythonPackage):
    """Triqler models identification and quantification error rates for
    label-free protein quantification experiments."""

    homepage = "https://github.com/statisticalbiotechnology/triqler"
    pypi = "triqler/triqler-0.6.2.tar.gz"

    license("Apache-2.0")

    version("0.6.2", sha256="09e0e286e252742be7fc957932eb1c998dce9d6d357b90473526ac7d6dc19d62")

    variant("distribution", default=False, description="Enable plotting helpers")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.12:", type=("build", "run"))
    depends_on("py-scipy@0.17:", type=("build", "run"))
    depends_on("py-threadpoolctl@1.0:", type=("build", "run"))
    depends_on("py-matplotlib@2.2:", type=("build", "run"), when="+distribution")

    @run_after("install")
    def install_test(self):
        python("-c", "import triqler")
