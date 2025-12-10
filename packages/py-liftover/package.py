# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLiftover(PythonPackage):
    """Lightweight interface to UCSC liftOver chain files."""

    homepage = "https://github.com/brentp/liftover"
    pypi = "liftover/liftover-1.3.3.tar.gz"

    version("1.3.3", sha256="4d6b3bf69d8fb5aff4b817f78eadea263ddbafaa53242436604e795a68691152")
    version(
        "1.3.1",
        sha256="43173ba201f2ad2ffd84c699b228d3f21da58e4d087d15d8bdcf600697ade10c",
        url="https://files.pythonhosted.org/packages/40/d3/4395023ec9bea950d18ebd960001467c44e6f581b316887b0abeaf024d80/liftover-1.3.1.tar.gz",
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-urllib3", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import liftover")
